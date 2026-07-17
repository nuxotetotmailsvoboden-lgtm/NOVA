import { ReactNode } from "react";

interface AuthLayoutProps {
  title: string;
  subtitle: string;
  children: ReactNode;
}

export default function AuthLayout({
  title,
  subtitle,
  children,
}: AuthLayoutProps) {
  return (
    <main className="auth-layout">
      <div className="auth-card">
        <div className="auth-header">
          <div className="auth-logo">NOVA</div>

          <h1>{title}</h1>

          <p>{subtitle}</p>
        </div>

        {children}
      </div>
    </main>
  );
}
