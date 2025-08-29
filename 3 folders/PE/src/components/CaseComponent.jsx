import React from 'react';
import { getCSRFToken } from '../utils/csrf'; // Make sure you have this helper or remove that line if unnecessary

const Case = ({ cases }) => {
  const handleAddCase = (caseId) => {
    fetch(`/save_case/${caseId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(), // optional, based on your setup
      },
      body: JSON.stringify({ id: caseId }),
    })
      .then((res) => {
        if (!res.ok) throw new Error('Failed to save case');
        alert('Case added successfully!');
      })
      .catch((err) => {
        console.error(err);
        alert('Error adding case');
      });
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Available Cases</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2' }}>
            <th style={thStyle}>Name</th>
            <th style={thStyle}>Case Type</th>
            <th style={thStyle}>Color</th>
            <th style={thStyle}>Power Supply</th>
            <th style={thStyle}>Side Panel</th>
            <th style={thStyle}>Internal Bays</th>
            <th style={thStyle}>Benchmark</th>
            <th style={thStyle}>Add</th>
          </tr>
        </thead>
        <tbody>
          {cases.map((pcCase) => (
            <tr key={pcCase.id}>
              <td style={tdStyle}>{pcCase.name}</td>
              <td style={tdStyle}>{pcCase.case_type}</td>
              <td style={tdStyle}>{pcCase.color}</td>
              <td style={tdStyle}>{pcCase.power_supply}</td>
              <td style={tdStyle}>{pcCase.side_panel}</td>
              <td style={tdStyle}>{pcCase.internal_bays}</td>
              <td style={tdStyle}>{pcCase.benchmark}</td>
              <td style={tdStyle}>
                <button
                  onClick={() => handleAddCase(pcCase.id)}
                  style={buttonStyle}
                >
                  Add Case
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const thStyle = {
  padding: '10px',
  textAlign: 'left',
  border: '1px solid black',
};

const tdStyle = {
  padding: '10px',
  textAlign: 'left',
  border: '1px solid black',
};

const buttonStyle = {
  backgroundColor: '#4CAF50',
  color: 'white',
  padding: '5px 10px',
  border: 'none',
  cursor: 'pointer',
};

export default Case;
