"use client";

import { ReactNode } from "react";

interface DeviceFrameProps {
  children: ReactNode;
  className?: string;
}

export default function DeviceFrame({
  children,
  className = "",
}: DeviceFrameProps) {
  return (
    <div className={`device-frame ${className}`}>
      <div className="device-screen">
        {children}
      </div>
    </div>
  );
}
