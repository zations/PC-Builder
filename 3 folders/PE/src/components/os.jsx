import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { getCSRFToken } from '../utils/csrf';

const OperatingSystems = () => {
  const [operatingSystems, setOperatingSystems] = useState([]);

  useEffect(() => {
    axios.get('/OS/')
      .then(res => setOperatingSystems(res.data))
      .catch(err => console.error('Failed to fetch OS list:', err));
  }, []);

  const handleAdd = (id) => {
    axios.post(`/save_os/${id}/`, null, {
      headers: {
        'X-CSRFToken': getCSRFToken(),
      }
    })
    .then(() => alert('Operating System added successfully!'))
    .catch(err => {
      console.error('Failed to add OS:', err);
      alert('Error adding Operating System.');
    });
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Available Operating Systems</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead className="bg-gray-800 text-gray-300">
            <tr>
              <th className="border border-gray-700 px-4 py-2">Name</th>
              <th className="border border-gray-700 px-4 py-2">Mode</th>
              <th className="border border-gray-700 px-4 py-2">Max Supported Memory</th>
              <th className="border border-gray-700 px-4 py-2">Benchmark</th>
              <th className="border border-gray-700 px-4 py-2">Add</th>
            </tr>
          </thead>
          <tbody>
            {operatingSystems.map((os) => (
              <tr key={os.id} className="hover:bg-gray-800">
                <td className="border border-gray-700 px-4 py-2">{os.name}</td>
                <td className="border border-gray-700 px-4 py-2">{os.mode}</td>
                <td className="border border-gray-700 px-4 py-2">{os.max_supported_memory} GB</td>
                <td className="border border-gray-700 px-4 py-2">{os.benchmark}</td>
                <td className="border border-gray-700 px-4 py-2">
                  <button
                    onClick={() => handleAdd(os.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-3 py-1 rounded"
                  >
                    Add OS
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

export default OperatingSystems;
