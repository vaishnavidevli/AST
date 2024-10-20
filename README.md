**Rule Engine with AST**

**Objective:**

Develop a 3-tier rule engine application that evaluates user eligibility based on attributes like age, department, income, and spend. The system will use an Abstract Syntax Tree (AST) to represent conditional rules and allow dynamic creation, combination, and modification of these rules.

**1.Project Setup**
   
Prerequisites:

IDE: PyCharm or any other IDE of your choice.

Python Version: 3.8+ (Make sure Python is installed, and you have set up a virtual environment if needed).

Initial Package Installations:
Install the necessary Python libraries:

**pip install Flask**

**pip install pymongo**

**pip install jsonschema**

2.**Running the Application:**

Clone the Repository:git clone https://github.com/vaishnavidevli/AST.git


Start the Application:

**python app.py**

**3.Stack Summary**

Frontend: HTML, CSS, JavaScript
Backend: Flask (Python), AST Parsing (Python)
Database: MongoDB
Testing: unittest (Python)
Package Management: pip

This main page provides a user interface for managing rules in a rule engine system. Users can:

1. **Create New Rules**: Input a rule string and submit it to the backend to create a new rule.
2. **View Existing Rules**: Display existing rules in a card format when the page loads.
3. **Update Rules**: Modify and update rules using an editable form.
4. **Delete Rules**: Remove rules using a delete button on each rule card.
5. **Evaluate Rules**: Evaluate a rule by providing user data, and get a result (True/False) based on whether the data matches the rule.

Each rule card provides options to update, delete, or evaluate the rule interactively.

Abstract Syntax Tree (AST) 

1. **Node Class**: Represents nodes in the AST with properties for type, value, and child nodes.

2. **create_rule Function**: Parses a rule string (e.g., `"age > 30 AND department = 'Sales'"`) to create an AST.

3. **combine_rules Function**: Combines multiple ASTs into a single AST using a specified operator (default is "AND").

4. **evaluate_rule Function**: Evaluates the AST against user data, returning a boolean result and detailed logs of the evaluation process.

5. **from_dict_to_node Function**: Converts a dictionary representation of a node back into a `Node` object.
   

**snapshots**

