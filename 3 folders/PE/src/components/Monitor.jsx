import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { getCSRFToken } from '../utils/csrf'; // ensure this function extracts the CSRF token

const Monitor = () => {
  const [monitors, setMonitors] = useState([]);

  useEffect(() => {
    axios.get('/Monitor/') // matches: path('Monitor/', views.Monitor_list_view, name='Monitors')
      .then(res => setMonitors(res.data))
      .catch(err => console.error('Error fetching monitors:', err));
  }, []);

  const handleAdd = (id) => {
    axios.post(`/save_Monitor/${id}/`, null, {
      headers: {
        'X-CSRFToken': getCSRFToken(),
      }
    })
    .then(() => alert('Monitor added successfully!'))
    .catch(err => {
      console.error('Error adding monitor:', err);
      alert('Failed to add monitor.');
    });
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h2 className="text-2xl font-bold mb-4">Available Monitors</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead className="bg-gray-800 text-gray-300">
            <tr>
              <th className="border border-gray-700 px-4 py-2">Name</th>
              <th className="border border-gray-700 px-4 py-2">Screen Size</th>
              <th className="border border-gray-700 px-4 py-2">Resolution</th>
              <th className="border border-gray-700 px-4 py-2">Refresh Rate</th>
              <th className="border border-gray-700 px-4 py-2">Response Time</th>
              <th className="border border-gray-700 px-4 py-2">Panel Type</th>
              <th className="border border-gray-700 px-4 py-2">Benchmark</th>
              <th className="border border-gray-700 px-4 py-2">Add</th>
            </tr>
          </thead>
          <tbody>
            {monitors.map((monitor) => (
              <tr key={monitor.id} className="hover:bg-gray-800">
                <td className="border border-gray-700 px-4 py-2">{monitor.name}</td>
                <td className="border border-gray-700 px-4 py-2">{monitor.screen_size}</td>
                <td className="border border-gray-700 px-4 py-2">{monitor.resolution}</td>
                <td className="border border-gray-700 px-4 py-2">{monitor.refresh_rate}</td>
                <td className="border border-gray-700 px-4 py-2">{monitor.response_time}</td>
                <td className="border border-gray-700 px-4 py-2">{monitor.panel_type}</td>
                <td className="border border-gray-700 px-4 py-2">{monitor.benchmark}</td>
                <td className="border border-gray-700 px-4 py-2">
                  <button
                    onClick={() => handleAdd(monitor.id)}
                    className="bg-green-600 hover:bg-green-500 text-white px-3 py-1 rounded"
                  >
                    Add Monitor
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

export default Monitor;
