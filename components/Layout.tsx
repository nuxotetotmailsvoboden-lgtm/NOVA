"use client";

import { ReactNode } from "react";

import Navbar from "./Navbar";
import Background from "./background/Background";

interface Props {
    children: ReactNode;
}

export default function Layout({ children }: Props) {
    return (
        <>
            <Background />

            <Navbar />

            <main className="nova-layout">
                {children}
            </main>
        </>
    );
}
