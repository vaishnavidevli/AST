from flask import Flask, request, jsonify, render_template
from rule_engine import create_rule, combine_rules, evaluate_rule, from_dict_to_node  # Import the rule functions
from db_config import db  # MongoDB database configuration
from flask_cors import CORS
from bson import ObjectId  # Import ObjectId for MongoDB queries
# import logging

app = Flask(__name__, template_folder='template')  # Specify the custom template folder
CORS(app)  # Enable CORS for all routes

# Enable logging for better debugging in case of errors
# logging.basicConfig(level=logging.DEBUG)

# Route to render the Create Rule page
@app.route('/')
def index():
    try:
        rules = list(db.rules.find())  # Fetch all rules from the database
        for rule in rules:
            rule['_id'] = str(rule['_id'])  # Convert ObjectId to string for JSON serialization
        return render_template('create_rule.html', rules=rules)  # Pass rules to the template
    except Exception as e:
        # logging.error(f"Error fetching rules: {str(e)}")
        return jsonify({"error": "Error fetching rules"}), 500

# Route to fetch all rules
@app.route('/get_rules', methods=['GET'])
def get_rules():
    try:
        rules = list(db.rules.find())  # Fetch all rules from the database
        for rule in rules:
            rule['_id'] = str(rule['_id'])  # Convert ObjectId to string for JSON serialization
        return jsonify({"rules": rules}), 200
    except Exception as e:
        return jsonify({"error": f"Error fetching rules: {str(e)}"}), 500


# Route to serve the Combine Rules page
# @app.route('/combine_rules_page')
# def combine_rules_page():
#     return render_template('combine_rules.html')  # Render the combine_rules.html template

# # Route to serve the Evaluate Rule page
@app.route('/evaluate_rule')
def evaluate_rule_page():
    return render_template('evaluate_rule.html')
# Render the evaluate_rule.html template


# Route to create a rule and store it in the database
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    try:
        rule_string = request.json.get('rule')
        if not rule_string:
            return jsonify({"error": "Rule string is required"}), 400

        ast = create_rule(rule_string)  # Generate AST from rule string
        rule_id = db.rules.insert_one({"rule": rule_string, "ast": ast.to_dict()}).inserted_id
        # logging.info(f"Rule created with ID: {rule_id}")
        return jsonify({"rule_id": str(rule_id)}), 201
    except Exception as e:
        # logging.error(f"Error creating rule: {str(e)}")
        return jsonify({"error": "Error creating rule"}), 500

# Route to update a rule
@app.route('/update_rule/<rule_id>', methods=['PUT'])
def update_rule(rule_id):
    try:
        rule_data = request.json.get('rule')  # Get the updated rule data from the request
        if not rule_data:
            return jsonify({"error": "Updated rule is required"}), 400

        # Update the rule in the database
        result = db.rules.update_one({"_id": ObjectId(rule_id)}, {"$set": {"rule": rule_data}})
        if result.matched_count == 0:
            return jsonify({"error": "Rule not found"}), 404

        return jsonify({"message": "Rule updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Error updating rule: {str(e)}"}), 500


# Route to get a rule by ID
@app.route('/get_rule/<rule_id>', methods=['GET'])
def get_rule(rule_id):
    try:
        rule = db.rules.find_one({"_id": ObjectId(rule_id)})
        if rule:
            rule['_id'] = str(rule['_id'])  # Convert ObjectId to string for JSON serialization
            return jsonify({"rule": rule}), 200
        return jsonify({"error": "Rule not found"}), 404
    except Exception as e:
        # logging.error(f"Error retrieving rule: {str(e)}")
        return jsonify({"error": f"Error retrieving rule: {str(e)}"}), 500

# Route to combine multiple rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    try:
        rules = request.json.get('rules')
        if not rules or not isinstance(rules, list):
            return jsonify({"error": "A list of rules is required"}), 400

        combined_ast = combine_rules(rules)
        # logging.info("Rules combined successfully")
        return jsonify({"ast": combined_ast.to_dict()}), 200
    except Exception as e:
        # logging.error(f"Error combining rules: {str(e)}")
        return jsonify({"error": "Error combining rules"}), 500



# Route to evaluate a rule based on user data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    try:
        rule_id = request.json.get('id')  # Receive rule ID
        user_data = request.json.get('data')

        if not rule_id or not user_data:
            return jsonify({"error": "Rule ID and user data are required"}), 400

        rule = db.rules.find_one({"_id": ObjectId(rule_id)})  # Fetch the rule from the database
        if not rule:
            return jsonify({"error": "Rule not found"}), 404

        ast = from_dict_to_node(rule['ast'])  # Convert AST dict to Node object
        result, evaluation_details = evaluate_rule(ast, user_data)  # Evaluate the rule

        # logging.info(f"Rule {rule_id} evaluated successfully")
        return jsonify({
            "result": result,
            "evaluationDetails": evaluation_details
        }), 200
    except Exception as e:
        # logging.error(f"Error evaluating rule: {str(e)}")
        return jsonify({"error": f"Error evaluating rule: {str(e)}"}), 500


# Route to delete a rule by its ID
@app.route('/delete_rule/<rule_id>', methods=['DELETE'])
def delete_rule(rule_id):
    try:
        result = db.rules.delete_one({"_id": ObjectId(rule_id)})  # Delete the rule from the database
        if result.deleted_count == 0:
            return jsonify({"error": "Rule not found"}), 404

        return jsonify({"message": "Rule deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Error deleting rule: {str(e)}"}), 500


# Enhanced security: setting up CSRF protection (optional)
# from flask_wtf.csrf import CSRFProtect
# csrf = CSRFProtect(app)
# csrf.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
