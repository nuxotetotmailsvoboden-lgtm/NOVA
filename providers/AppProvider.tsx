"use client";

import { ReactNode } from "react";

import QueryProvider from "./QueryProvider";

import { useAuth } from "@/lib/hooks/useAuth";

interface AppProviderProps {
  children: ReactNode;
}

function Bootstrap({
  children,
}: {
  children: ReactNode;
}) {
  useAuth();

  return <>{children}</>;
}

export default function AppProvider({
  children,
}: AppProviderProps) {
  return (
    <QueryProvider>
      <Bootstrap>
        {children}
      </Bootstrap>
    </QueryProvider>
  );
}
