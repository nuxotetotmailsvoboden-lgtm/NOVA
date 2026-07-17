"use client";

import { ReactNode } from "react";
import Navbar from "./Navbar";

interface Props {
  children: ReactNode;
}

export default function Layout({ children }: Props) {
  return (
    <>
      <Navbar />

      <main className="nova-layout">
        {children}
      </main>
    </>
  );
}
