"use client";

import { ReactNode } from "react";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

interface Props {
  children: ReactNode;
}

export default function DashboardLayout({ children }: Props) {
  return (
    <div className="dashboard-app">

      <Sidebar />

      <div className="dashboard-main">

        <Topbar />

        <main className="dashboard-page">
          {children}
        </main>

      </div>

    </div>
  );
}
