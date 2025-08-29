import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { getCSRFToken } from '../utils/csrf';

const Motherboard = () => {
  const [motherboards, setMotherboards] = useState([]);

  useEffect(() => {
    axios.get('/motherboard/') // Matches Django: path('motherboard/', ...)
      .then(res => setMotherboards(res.data))
      .catch(err => console.error('Failed to fetch motherboards:', err));
  }, []);

  const handleAdd = (id) => {
    axios.post(`/save_motherboard/${id}/`, null, {
      headers: {
        'X-CSRFToken': getCSRFToken(),
      }
    })
    .then(() => alert('Motherboard added successfully!'))
    .catch(err => {
      console.error('Failed to add motherboard:', err);
      alert('Error adding motherboard.');
    });
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Available Motherboards</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead className="bg-gray-800 text-gray-300">
            <tr>
              <th className="border border-gray-700 px-4 py-2">Name</th>
              <th className="border border-gray-700 px-4 py-2">Socket</th>
              <th className="border border-gray-700 px-4 py-2">Form Factor</th>
              <th className="border border-gray-700 px-4 py-2">Memory Max</th>
              <th className="border border-gray-700 px-4 py-2">Memory Slots</th>
              <th className="border border-gray-700 px-4 py-2">Benchmark</th>
              <th className="border border-gray-700 px-4 py-2">Add</th>
            </tr>
          </thead>
          <tbody>
            {motherboards.map((mb) => (
              <tr key={mb.id} className="hover:bg-gray-800">
                <td className="border border-gray-700 px-4 py-2">{mb.name}</td>
                <td className="border border-gray-700 px-4 py-2">{mb.socket_cpu}</td>
                <td className="border border-gray-700 px-4 py-2">{mb.form_factor}</td>
                <td className="border border-gray-700 px-4 py-2">{mb.memory_max} GB</td>
                <td className="border border-gray-700 px-4 py-2">{mb.memory_slots}</td>
                <td className="border border-gray-700 px-4 py-2">{mb.benchmark}</td>
                <td className="border border-gray-700 px-4 py-2">
                  <button
                    onClick={() => handleAdd(mb.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-3 py-1 rounded"
                  >
                    Add Motherboard
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

export default Motherboard;
