import "./globals.css";

import type { Metadata } from "next";
import AppProvider from "@/providers/AppProvider";

export const metadata: Metadata = {
  title: "NOVA",
  description: "Business OS",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ru">
      <body>
        <AppProvider>
          {children}
        </AppProvider>
      </body>
    </html>
  );
}
