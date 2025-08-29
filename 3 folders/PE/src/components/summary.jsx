import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Summary = () => {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    axios.get('/api/summary/')
      .then(res => setSummary(res.data))
      .catch(err => console.error('Error fetching summary:', err));
  }, []);

  if (!summary) {
    return <div className="text-white p-6">Loading summary...</div>;
  }

  const {
    performance_score,
    cooling_recommendations,
    total_power,
    pc_build,
    compatibility_report,
  } = summary;

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <h2 className="text-3xl font-bold mb-4 text-green-400">Your PC Build</h2>
      <p><strong>Performance Score:</strong> {performance_score}</p>
      <p><strong>Cooling Recommendations:</strong> {cooling_recommendations}</p>
      <p><strong>Total Power Needed:</strong> {total_power} W</p>

      <div className="overflow-x-auto mt-6">
        <table className="min-w-full border border-gray-700 text-sm">
          <thead className="bg-gray-800 text-gray-300">
            <tr>
              <th className="border border-gray-700 px-4 py-2">Component</th>
              <th className="border border-gray-700 px-4 py-2">Selection</th>
            </tr>
          </thead>
          <tbody>
            <tr><td className="border border-gray-700 px-4 py-2">CPU</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_cpu}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">CPU Cooler</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_cpu_cooler}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">Motherboard</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_motherboard}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">Memory</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_ram}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">Storage</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_storage}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">Video Card</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_gpu}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">Case</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_case}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">Power Supply</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_psu}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">OS</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_os}</td></tr>
            <tr><td className="border border-gray-700 px-4 py-2">Monitor</td><td className="border border-gray-700 px-4 py-2">{pc_build.selected_monitor}</td></tr>
          </tbody>
        </table>
      </div>

      <h3 className="text-2xl mt-8 mb-2">Compatibility Report</h3>
      <p className="text-gray-300">{compatibility_report}</p>
    </div>
  );
};

export default Summary;
