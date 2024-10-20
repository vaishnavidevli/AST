import React, { useState } from 'react';

function RuleForm() {
  const [rule, setRule] = useState('');

  const submitRule = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/create_rule', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ rule }),
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data);
    } else {
      console.error("Error:", await response.json());
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
