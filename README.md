**Youtube link of the working solution**
https://www.youtube.com/watch?v=2nEyDwixDcw 


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

![Screenshot (2689)](https://github.com/user-attachments/assets/2ec28a95-0e60-48b2-b4e7-a7395b1d0ebc)


![Screenshot (2690)](https://github.com/user-attachments/assets/84bf82bb-cbb2-424d-8b98-538a73e75455)


![Screenshot (2691)](https://github.com/user-attachments/assets/cfc70bd6-f9c0-4107-b9a9-b2c1b2a5a9b6)


![Screenshot (2692)](https://github.com/user-attachments/assets/3a924358-31e9-48d0-80c2-4a1ee1967078)



![Screenshot (2693)](https://github.com/user-attachments/assets/038312e3-8b16-4167-9940-d84f5627380f)



![Screenshot (2694)](https://github.com/user-attachments/assets/654f565a-af57-4e45-aa8c-64359f13c030)



![Screenshot (2695)](https://github.com/user-attachments/assets/cf6d9d3c-3dd8-4a7c-b0b1-ed8bd1b88251)


![Screenshot (2696)](https://github.com/user-attachments/assets/d72de74e-ae96-4936-b8b9-3e26b19c17b3)


![Screenshot (2697)](https://github.com/user-attachments/assets/a0e4859b-9ba4-4584-820d-82a3b9019af7)


![Screenshot (2698)](https://github.com/user-attachments/assets/557dc676-bd25-4e87-a437-cda1516ab64f)



![Screenshot (2699)](https://github.com/user-attachments/assets/b0bca43b-c0a7-4649-b616-1516b14740f5)


![Screenshot (2688)](https://github.com/user-attachments/assets/37042142-daca-456a-b21f-323002685fe6)


![Screenshot (2687)](https://github.com/user-attachments/assets/35bed259-adcc-4617-a4f3-a99176f21095)

