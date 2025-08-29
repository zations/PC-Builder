import React from 'react';
import { getCSRFToken } from '../utils/csrf';

const CpuCooler = ({ cpuCoolers }) => {
  const handleAddCooler = (coolerId) => {
    fetch(`/save_cpu_cooler/${coolerId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),
      },
      body: JSON.stringify({ id: coolerId }),
    })
      .then((res) => {
        if (!res.ok) throw new Error('Failed to save CPU Cooler');
        return res.json();
      })
      .then(() => {
        alert('CPU Cooler added successfully!');
      })
      .catch((err) => {
        console.error(err);
        alert('Error adding CPU Cooler');
      });
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <h2 className="text-3xl font-bold mb-6">Available CPU Coolers</h2>

      <div className="overflow-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead>
            <tr className="bg-gray-800 text-gray-300">
              <th className="px-4 py-2 border border-gray-700">Name</th>
              <th className="px-4 py-2 border border-gray-700">Type</th>
              <th className="px-4 py-2 border border-gray-700">TDP Support (W)</th>
              <th className="px-4 py-2 border border-gray-700">Fan Size</th>
              <th className="px-4 py-2 border border-gray-700">Socket Compatibility</th>
              <th className="px-4 py-2 border border-gray-700">Benchmark</th>
              <th className="px-4 py-2 border border-gray-700">Add</th>
            </tr>
          </thead>
          <tbody>
            {cpuCoolers.map((cooler) => (
              <tr key={cooler.id} className="hover:bg-gray-800">
                <td className="px-4 py-2 border border-gray-700">{cooler.name}</td>
                <td className="px-4 py-2 border border-gray-700">{cooler.cooler_type}</td>
                <td className="px-4 py-2 border border-gray-700">{cooler.tdp} W</td>
                <td className="px-4 py-2 border border-gray-700">{cooler.fan_size}</td>
                <td className="px-4 py-2 border border-gray-700">{cooler.socket_compatibility}</td>
                <td className="px-4 py-2 border border-gray-700">{cooler.benchmark}</td>
                <td className="px-4 py-2 border border-gray-700">
                  <button
                    onClick={() => handleAddCooler(cooler.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-4 py-1 rounded"
                  >
                    Add Cooler
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

export default CpuCooler;
