"use client";

import { useEffect, useState } from "react";

export default function Splash() {
  const [show, setShow] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShow(true);
    }, 250);

    return () => clearTimeout(timer);
  }, []);

  return (
    <section className="nova-splash">

      <div className="nova-background"></div>

      <div className={`nova-content ${show ? "show" : ""}`}>

        <div className="nova-logo">
          N
        </div>

        <h1 className="nova-title">
          NOVA
        </h1>

        <p className="nova-subtitle">
          Premium Telegram Automation
        </p>

      </div>

    </section>
  );
}
