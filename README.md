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

![Screenshot (2677)](https://github.com/user-attachments/assets/01cf1d09-80fd-4450-af35-1596ab15040b)


![Screenshot (2678)](https://github.com/user-attachments/assets/54e62164-6453-4be4-9359-995f7bb5bb40)


![Screenshot (2679)](https://github.com/user-attachments/assets/6200b558-c182-4d1c-a145-9db3b4d2b2e8)


![Screenshot (2680)](https://github.com/user-attachments/assets/cc38f21f-d75d-4f62-af67-aaa9a38dbd5a)


![Screenshot (2681)](https://github.com/user-attachments/assets/b94fa5a6-57d3-452a-a185-56e1006fc632)


![Screenshot (2682)](https://github.com/user-attachments/assets/d44faec5-60c9-4fcc-b3a5-1d662e97adf3)


![Screenshot (2683)](https://github.com/user-attachments/assets/8892b5b9-ca24-4f7a-b9b4-5c6c0ed2fd90)


![Screenshot (2684)](https://github.com/user-attachments/assets/14dabe14-7a64-46e7-9917-e81fa40bc0fb)


![Screenshot (2685)](https://github.com/user-attachments/assets/30623a99-3b94-4197-92fd-62f0a3b23e2f)


![Screenshot (2686)](https://github.com/user-attachments/assets/fa406489-40cd-49f0-8c19-7e3b0960fe35)


![Screenshot (2687)](https://github.com/user-attachments/assets/b183fc5a-ced4-451a-a392-fa8ae0caf473)


![Screenshot (2688)](https://github.com/user-attachments/assets/cf9364a9-f4a7-4ae7-b550-eb845bd16c03)

