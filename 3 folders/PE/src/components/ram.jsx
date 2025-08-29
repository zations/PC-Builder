import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { getCSRFToken } from '../utils/csrf';

const Ram = () => {
  const [rams, setRams] = useState([]);

  useEffect(() => {
    axios.get('/RAM/')
      .then(res => setRams(res.data))
      .catch(err => console.error('Error fetching RAMs:', err));
  }, []);

  const handleAdd = (id) => {
    axios.post(`/save_ram/${id}/`, null, {
      headers: {
        'X-CSRFToken': getCSRFToken(),
      }
    })
    .then(() => alert('RAM added successfully!'))
    .catch(err => {
      console.error('Failed to add RAM:', err);
      alert('Error adding RAM.');
    });
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Available RAM</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead className="bg-gray-800 text-gray-300">
            <tr>
              <th className="border border-gray-700 px-4 py-2">Name</th>
              <th className="border border-gray-700 px-4 py-2">Speed</th>
              <th className="border border-gray-700 px-4 py-2">Modules</th>
              <th className="border border-gray-700 px-4 py-2">CAS Latency</th>
              <th className="border border-gray-700 px-4 py-2">First Word Latency</th>
              <th className="border border-gray-700 px-4 py-2">Benchmark</th>
              <th className="border border-gray-700 px-4 py-2">Add</th>
            </tr>
          </thead>
          <tbody>
            {rams.map((ram) => (
              <tr key={ram.id} className="hover:bg-gray-800">
                <td className="border border-gray-700 px-4 py-2">{ram.name}</td>
                <td className="border border-gray-700 px-4 py-2">{ram.speed} MHz</td>
                <td className="border border-gray-700 px-4 py-2">{ram.modules}</td>
                <td className="border border-gray-700 px-4 py-2">{ram.cas_latency}</td>
                <td className="border border-gray-700 px-4 py-2">{ram.first_word_latency}</td>
                <td className="border border-gray-700 px-4 py-2">{ram.benchmark}</td>
                <td className="border border-gray-700 px-4 py-2">
                  <button
                    onClick={() => handleAdd(ram.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-3 py-1 rounded"
                  >
                    Add RAM
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

export default Ram;
