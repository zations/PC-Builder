import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Helper to get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const trimmed = cookie.trim();
      if (trimmed.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(trimmed.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const Gpu = () => {
  const [gpus, setGpus] = useState([]);

  useEffect(() => {
    axios.get('/gpu/')
      .then((res) => setGpus(res.data))
      .catch((err) => console.error('Error fetching GPUs:', err));
  }, []);

  const handleAddGpu = (gpuId) => {
    axios.post(`/save_gpu/${gpuId}/`, null, {
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
    })
    .then(() => alert('GPU added successfully!'))
    .catch((err) => {
      console.error('Error adding GPU:', err);
      alert('Failed to add GPU.');
    });
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <h2 className="text-3xl font-bold mb-6">Available Video Cards</h2>

      <div className="overflow-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead>
            <tr className="bg-gray-800 text-gray-300">
              <th className="px-4 py-2 border border-gray-700">Name</th>
              <th className="px-4 py-2 border border-gray-700">G3Mark</th>
              <th className="px-4 py-2 border border-gray-700">G2Mark</th>
              <th className="px-4 py-2 border border-gray-700">TDP</th>
              <th className="px-4 py-2 border border-gray-700">Price</th>
              <th className="px-4 py-2 border border-gray-700">Add</th>
            </tr>
          </thead>
          <tbody>
            {gpus.map((gpu) => (
              <tr key={gpu.id} className="hover:bg-gray-800">
                <td className="px-4 py-2 border border-gray-700">{gpu.name}</td>
                <td className="px-4 py-2 border border-gray-700">{gpu.G3mark}</td>
                <td className="px-4 py-2 border border-gray-700">{gpu.G2mark}</td>
                <td className="px-4 py-2 border border-gray-700">{gpu.Tdp}</td>
                <td className="px-4 py-2 border border-gray-700">{gpu.Price}</td>
                <td className="px-4 py-2 border border-gray-700">
                  <button
                    onClick={() => handleAddGpu(gpu.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-4 py-1 rounded"
                  >
                    Add GPU
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

export default Gpu;
