const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const { create_rule, combine_rules, evaluate_rule } = require('./rule_engine');
const MongoClient = require('mongodb').MongoClient;
const { ObjectId } = require('mongodb');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, 'backend')));

// MongoDB connection
const uri = process.env.MONGO_URI || 'mongodb://localhost:27017/';
let db;

MongoClient.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(client => {
    db = client.db('rule_engine');
    console.log('Connected to Database');
  })
  .catch(error => console.error(error));

// Serve the Create Rule page
app.get('/create_rule_page', (req, res) => {
  res.sendFile(path.join(__dirname, 'template/create_rule.html'));
});

// Serve the Combine Rules page
app.get('/combine_rules_page', (req, res) => {
  res.sendFile(path.join(__dirname, 'template/combine_rules.html'));
});

// Serve the Evaluate page
app.get('/evaluate.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'template/evaluate.html')); // Ensure the path is correct
});

// Create a rule and store it in the database
app.post('/create_rule', (req, res) => {
  const rule_string = req.body.rule;
  const ast = create_rule(rule_string);

  db.collection('rules').insertOne({ rule: rule_string, ast: ast })
    .then(result => {
      res.status(201).json({ rule_id: result.insertedId });
    })
    .catch(error => {
      res.status(500).json({ error: 'Failed to insert rule' });
    });
});

// Combine multiple rules
app.post('/combine_rules', (req, res) => {
  const rules = req.body.rules;
  const combined_ast = combine_rules(rules);
  res.json({ ast: combined_ast });
});

// Evaluate a rule based on user data
app.post('/evaluate_rule', (req, res) => {
  const rule_ast = req.body.ast;
  const user_data = req.body.data;
  const result = evaluate_rule(rule_ast, user_data);
  res.json({ result });
});

// Get all rules
app.get('/get_rules', (req, res) => {
  db.collection('rules').find().toArray()
    .then(rules => res.json({ rules }))
    .catch(error => res.status(500).json({ error: 'Failed to fetch rules' }));
});

// Update a rule
app.put('/update_rule/:id', (req, res) => {
  const ruleId = req.params.id;
  const updatedRule = req.body.rule;

  db.collection('rules').updateOne({ _id: ObjectId(ruleId) }, { $set: { rule: updatedRule } })
    .then(result => {
      if (result.modifiedCount > 0) {
        res.json({ message: 'Rule updated successfully' });
      } else {
        res.status(404).json({ error: 'Rule not found' });
      }
    })
    .catch(error => res.status(500).json({ error: 'Failed to update rule' }));
});

// Delete a rule
app.delete('/delete_rule/:id', (req, res) => {
  const ruleId = req.params.id;

  db.collection('rules').deleteOne({ _id: ObjectId(ruleId) })
    .then(result => {
      if (result.deletedCount > 0) {
        res.json({ message: 'Rule deleted successfully' });
      } else {
        res.status(404).json({ error: 'Rule not found' });
      }
    })
    .catch(error => res.status(500).json({ error: 'Failed to delete rule' }));
});

app.get('/tree.html', (req, res) => {
    const ast = req.query.ast; // Get the AST from the query parameter
    res.render('tree', { ast: ast }); // Render the tree.html template with the AST
});


// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});


