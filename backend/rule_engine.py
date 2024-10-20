# Define the Node class for the Abstract Syntax Tree (AST)
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # Use 'node_type' to avoid confusion with built-in 'type'
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        """Convert the Node to a dictionary for MongoDB storage."""
        return {
            "type": self.type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }


# Function to create a rule (AST representation)
def create_rule(rule_string):
    # Handle parentheses by splitting tokens carefully
    tokens = rule_string.replace('(', ' ( ').replace(')', ' ) ').split()
    stack = []  # Ensure this is defined as a list
    current_operand = []

    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            # Pop and build expressions until the last '('
            operand = ' '.join(current_operand) if current_operand else None
            if operand:
                stack.append(Node(node_type="operand", value=operand))
                current_operand = []
            sub_expr = []
            while stack and stack[-1] != '(':
                sub_expr.insert(0, stack.pop())
            stack.pop()  # Pop the '('
            # Now build the subexpression AST
            if len(sub_expr) == 3:  # binary expression
                right = sub_expr.pop()
                op = sub_expr.pop().value  # Operator node's value
                left = sub_expr.pop()
                stack.append(Node(node_type="operator", value=op, left=left, right=right))
        elif token in ['AND', 'OR']:
            # If we hit an operator, we need to close the current operand
            if current_operand:
                operand = ' '.join(current_operand)  # Join the current operand parts
                stack.append(Node(node_type="operand", value=operand))
                current_operand = []  # Reset for next operand
            # Create the operator node
            stack.append(Node(node_type="operator", value=token))
        else:
            current_operand.append(token)  # Build the operand incrementally

    # If there's a remaining operand at the end, add it to the stack
    if current_operand:
        operand = ' '.join(current_operand)
        stack.append(Node(node_type="operand", value=operand))

    # Handle remaining nodes in the stack
    while len(stack) > 1:
        right = stack.pop()
        operator_node = stack.pop()
        left = stack.pop()
        operator_node.left = left
        operator_node.right = right
        stack.append(operator_node)

    return stack[0] if stack else None


# Function to combine multiple rules into a single AST
def combine_rules(rules, combine_operator="AND"):
    combined_ast = None
    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node(node_type="operator", left=combined_ast, right=ast, value=combine_operator)
    return combined_ast


# Function to evaluate a rule based on user data and collect evaluation details
def evaluate_rule(ast, data, details=None):
    if details is None:
        details = []

    if ast.type == "operand":
        try:
            # Remove parentheses from the operand and split by spaces
            field, operator, value = ast.value.replace("(", "").replace(")", "").split()

            if value.isdigit():
                value = int(value)
            else:
                value = value.strip("'")  # Handle string values

            # Log the evaluation details
            if field not in data:
                details.append(f"Field '{field}' not found in user data.")
                return False, details

            # Check the condition based on the operator
            if operator == '>':
                result = data[field] > value
            elif operator == '=':
                result = data[field] == value
            elif operator == '<':
                result = data[field] < value
            elif operator == '>=':
                result = data[field] >= value
            elif operator == '<=':
                result = data[field] <= value
            elif operator == '!=':
                result = data[field] != value
            else:
                details.append(f"Unknown operator '{operator}'")
                result = False

            details.append(f"Evaluated: {field} {operator} {value} with user data {data[field]} -> {result}")
            return result, details

        except ValueError:
            details.append("Error: The operand must be in the format 'field operator value'.")
            return False, details
        except Exception as e:
            details.append(f"Error evaluating operand: {str(e)}")
            return False, details

    elif ast.type == "operator":
        left_eval, details = evaluate_rule(ast.left, data, details) if ast.left else (False, details)
        right_eval, details = evaluate_rule(ast.right, data, details) if ast.right else (False, details)

        if ast.value == "AND":
            result = left_eval and right_eval
        elif ast.value == "OR":
            result = left_eval or right_eval
        else:
            result = False

        details.append(f"Evaluated operator '{ast.value}' -> {result}")
        return result, details

    return False, details


# Function to convert a dictionary back to a Node object
def from_dict_to_node(ast_dict):
    """Convert a dictionary representation of a node back to a Node object."""
    left = from_dict_to_node(ast_dict['left']) if ast_dict['left'] else None
    right = from_dict_to_node(ast_dict['right']) if ast_dict['right'] else None
    return Node(node_type=ast_dict['type'], value=ast_dict['value'], left=left, right=right)


# Example Usage and Testing
if __name__ == "__main__":
    # Example rule
    rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"

    # Create the rule's AST
    combined_rule = create_rule(rule_string)

    # Example: Combine two rules
    rules = [
        "age > 30 AND department = 'Sales'",
        "salary > 50000 OR experience > 5"
    ]
    combined_ast = combine_rules(rules)

    # User data for evaluation
    user_data = {
        "age": 32,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
    }

    # Evaluate the combined rule
    result, evaluation_details = evaluate_rule(combined_rule, user_data)

    print("Final Evaluation Result:", result)
    print("Evaluation Details:")
    for detail in evaluation_details:
        print(detail)

    # Convert to dict and back to AST
    ast_dict = combined_rule.to_dict()
    restored_ast = from_dict_to_node(ast_dict)

    # Evaluate again using the restored AST
    result_restored, evaluation_details_restored = evaluate_rule(restored_ast, user_data)

    print("\nFinal Evaluation Result (Restored AST):", result_restored)
    print("Evaluation Details (Restored AST):")
    for detail in evaluation_details_restored:
        print(detail)
