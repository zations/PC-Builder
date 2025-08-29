import React from 'react';
import { useNavigate } from 'react-router-dom';


const Home = () => {
  const navigate = useNavigate();

  const parts = [
    { label: 'CPU', route: '/cpu' },
    { label: 'CPU Cooler', route: '/cpucooler' },
    { label: 'Motherboard', route: '/motherboard' },
    { label: 'Memory', route: '/ram' },
    { label: 'Storage', route: '/storage' },
    { label: 'Video Card', route: '/gpu' },
    { label: 'Case', route: '/case' },
    { label: 'Power Supply', route: '/powersupply' },
    { label: 'OS', route: '/os' },
    { label: 'Monitor', route: '/monitor' },
  ];

  return (
    <div>
      {/* Navigation Header */}
      <header>
        <div className="logo">
          <h1>PCPARTPICKER</h1>
        </div>
        <nav>
          <ul>
            <li><a href="#">Builder</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">Guides</a></li>
            <li><a href="#">Completed Builds</a></li>
            <li><a href="#">Trends</a></li>
            <li><a href="#">Benchmarks</a></li>
            <li><a href="#">Forums</a></li>
          </ul>
        </nav>
        <div className="auth-links">
          <a href="#">Log In</a>
          <a href="#">Register</a>
        </div>
      </header>

      {/* Main Section */}
      <section className="main-section">
        <h2>Choose Your Parts</h2>

        <div className="parts-selection">
          <table>
            <thead>
              <tr>
                <th>Component</th>
                <th>Selection</th>
              </tr>
            </thead>
            <tbody>
              {parts.map((part) => (
                <tr key={part.label}>
                  <td>{part.label}</td>
                  <td>
                    <button onClick={() => navigate(part.route)}>
                      Choose A {part.label}
                    </button>
                  </td>
                  {/* extra empty <td> for structure */}
                  {Array(6).fill(null).map((_, i) => <td key={i}></td>)}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
};

export default Home;
