// src/App.js
import React from 'react';
import RuleForm from './components/RuleForm';

function App() {
  return (
    <div>
      <h1>Rule Engine</h1>
      <RuleForm />
    </div>
  );
}

export default App;

// src/components/RuleForm.js
import React, { useState } from 'react';

function RuleForm() {
  const [rule, setRule] = useState('');

  const submitRule = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/create_rule', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={submitRule}>
      <label>Enter Rule:</label>
      <input
        type="text"
        value={rule}
        onChange={(e) => setRule(e.target.value)}
      />
      <button type="submit">Submit Rule</button>
    </form>
  );
}

export default RuleForm;
