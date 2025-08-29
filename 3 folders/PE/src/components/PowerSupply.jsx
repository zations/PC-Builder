import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { getCSRFToken } from '../utils/csrf';

const PowerSupply = () => {
  const [psus, setPsus] = useState([]);

  useEffect(() => {
    axios.get('/Powersupply/')
      .then(res => setPsus(res.data))
      .catch(err => console.error('Failed to fetch PSUs:', err));
  }, []);

  const handleAdd = (id) => {
    axios.post(`/save_psu/${id}/`, null, {
      headers: {
        'X-CSRFToken': getCSRFToken(),
      }
    })
    .then(() => alert('Power Supply added successfully!'))
    .catch(err => {
      console.error('Error adding Power Supply:', err);
      alert('Failed to add Power Supply.');
    });
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Available Power Supplies</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead className="bg-gray-800 text-gray-300">
            <tr>
              <th className="border border-gray-700 px-4 py-2">Name</th>
              <th className="border border-gray-700 px-4 py-2">Efficiency Rating</th>
              <th className="border border-gray-700 px-4 py-2">Wattage</th>
              <th className="border border-gray-700 px-4 py-2">Modular</th>
              <th className="border border-gray-700 px-4 py-2">Benchmark</th>
              <th className="border border-gray-700 px-4 py-2">Add</th>
            </tr>
          </thead>
          <tbody>
            {psus.map((psu) => (
              <tr key={psu.id} className="hover:bg-gray-800">
                <td className="border border-gray-700 px-4 py-2">{psu.name}</td>
                <td className="border border-gray-700 px-4 py-2">{psu.efficiency_rating}</td>
                <td className="border border-gray-700 px-4 py-2">{psu.wattage} W</td>
                <td className="border border-gray-700 px-4 py-2">{psu.modular ? 'Yes' : 'No'}</td>
                <td className="border border-gray-700 px-4 py-2">{psu.benchmark}</td>
                <td className="border border-gray-700 px-4 py-2">
                  <button
                    onClick={() => handleAdd(psu.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-3 py-1 rounded"
                  >
                    Add PSU
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default PowerSupply;
