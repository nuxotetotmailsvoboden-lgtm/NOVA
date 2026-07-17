"use client";

import DeviceFrame from "./DeviceFrame";

export default function Phone() {
  return (
    <DeviceFrame className="phone">

      <div className="telegram-header">
        NOVA Mini App
      </div>

      <div className="telegram-card">
        AI Assistant
      </div>

      <div className="telegram-card">
        Portfolio
      </div>

      <div className="telegram-card">
        CRM
      </div>

      <button className="telegram-button">
        Open
      </button>

    </DeviceFrame>
  );
}
