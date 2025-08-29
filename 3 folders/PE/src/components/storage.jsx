import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { getCSRFToken } from '../utils/csrf';

const Storage = () => {
  const [storages, setStorages] = useState([]);

  useEffect(() => {
    axios.get('/storage/')
      .then(res => setStorages(res.data))
      .catch(err => console.error('Error fetching storages:', err));
  }, []);

  const handleAdd = (id) => {
    axios.post(`/save_storage/${id}/`, null, {
      headers: {
        'X-CSRFToken': getCSRFToken(),
      }
    })
    .then(() => alert('Storage added successfully!'))
    .catch(err => {
      console.error('Error adding storage:', err);
      alert('Failed to add storage.');
    });
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Available Storage</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead className="bg-gray-800 text-gray-300">
            <tr>
              <th className="border border-gray-700 px-4 py-2">Name</th>
              <th className="border border-gray-700 px-4 py-2">Capacity</th>
              <th className="border border-gray-700 px-4 py-2">Type</th>
              <th className="border border-gray-700 px-4 py-2">Form Factor</th>
              <th className="border border-gray-700 px-4 py-2">Interface</th>
              <th className="border border-gray-700 px-4 py-2">Benchmark</th>
              <th className="border border-gray-700 px-4 py-2">Add</th>
            </tr>
          </thead>
          <tbody>
            {storages.map((storage) => (
              <tr key={storage.id} className="hover:bg-gray-800">
                <td className="border border-gray-700 px-4 py-2">{storage.name}</td>
                <td className="border border-gray-700 px-4 py-2">{storage.capacity}</td>
                <td className="border border-gray-700 px-4 py-2">{storage.storage_type}</td>
                <td className="border border-gray-700 px-4 py-2">{storage.form_factor}</td>
                <td className="border border-gray-700 px-4 py-2">{storage.interface}</td>
                <td className="border border-gray-700 px-4 py-2">{storage.benchmark}</td>
                <td className="border border-gray-700 px-4 py-2">
                  <button
                    onClick={() => handleAdd(storage.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-3 py-1 rounded"
                  >
                    Add Storage
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

export default Storage;
