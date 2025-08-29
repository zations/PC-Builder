import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import CPU from './components/CPU';
import GPU from './components/GPU';
import Monitor from './components/Monitor';
import Motherboard from './components/Motherboard';
import PowerSupply from './components/PowerSupply';
import RAM from './components/RAM';
import Storage from './components/Storage';
import OSComponent from "./components/os";
import CaseComponent from './components/CaseComponent';
import Summary from './components/Summary';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/cpu" element={<CPU />} />
      <Route path="/gpu" element={<GPU />} />
      <Route path="/monitor" element={<Monitor />} />
      <Route path="/motherboard" element={<Motherboard />} />
      <Route path="/powersupply" element={<PowerSupply />} />
      <Route path="/ram" element={<RAM />} />
      <Route path="/storage" element={<Storage />} />
      <Route path="/os" element={<OSComponent />} />
      <Route path="/case" element={<CaseComponent />} />
      <Route path="/summary" element={<Summary />} />
    </Routes>
  );
};

export default App;
