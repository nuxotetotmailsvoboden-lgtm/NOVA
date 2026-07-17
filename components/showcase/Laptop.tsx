"use client";

import DeviceFrame from "./DeviceFrame";

export default function Laptop() {
  return (
    <DeviceFrame className="laptop">

      <div className="mock-navbar">
        <div className="mock-logo">NOVA</div>

        <div className="mock-menu">
          <span>Services</span>
          <span>Portfolio</span>
          <span>CRM</span>
          <span>AI</span>
        </div>
      </div>

      <div className="mock-content">

        <div className="mock-chart"></div>

        <div className="mock-cards">

          <div className="mini-card"></div>

          <div className="mini-card"></div>

          <div className="mini-card"></div>

        </div>

      </div>

    </DeviceFrame>
  );
}
