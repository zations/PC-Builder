import React, { useEffect, useState } from 'react';
import axios from 'axios';

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

const CPU = () => {
  const [cpus, setCpus] = useState([]);

  useEffect(() => {
    axios.get('/cpu/')
      .then(res => setCpus(res.data))
      .catch(err => console.error('Error fetching CPUs:', err));
  }, []);

  const handleAddCPU = (cpuId) => {
    axios.post(`/save_cpu/${cpuId}/`, null, {
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
    })
    .then(() => alert("CPU added successfully"))
    .catch(err => alert("Failed to add CPU"));
  };

  return (
    <div>
      <h2>Available CPUs</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Cores</th>
            <th>Threads</th>
            <th>Base Clock</th>
            <th>Boost Clock</th>
            <th>TDP</th>
            <th>Price</th>
            <th>Benchmark</th>
            <th>Add</th>
          </tr>
        </thead>
        <tbody>
          {cpus.map(cpu => (
            <tr key={cpu.id}>
              <td>{cpu.name}</td>
              <td>{cpu.cores}</td>
              <td>{cpu.threads}</td>
              <td>{cpu.base_clock}</td>
              <td>{cpu.boost_clock}</td>
              <td>{cpu.tdp}</td>
              <td>{cpu.price}</td>
              <td>{cpu.benchmark}</td>
              <td>
                <button onClick={() => handleAddCPU(cpu.id)}>
                  Add CPU
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CPU;
