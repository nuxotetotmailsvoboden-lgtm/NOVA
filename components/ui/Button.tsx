"use client";

import React from "react";

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "ghost";
  loading?: boolean;
}

export default function Button({
  children,
  variant = "primary",
  loading = false,
  className = "",
  ...props
}: ButtonProps) {
  return (
    <button
      className={`nova-btn nova-btn-${variant} ${className}`}
      disabled={loading || props.disabled}
      {...props}
    >
      {loading ? "Загрузка..." : children}
    </button>
  );
}
