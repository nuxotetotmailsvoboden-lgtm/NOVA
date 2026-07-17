"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const menu = [
  { title: "Dashboard", href: "/dashboard", icon: "🏠" },
  { title: "AI Assistant", href: "/dashboard/ai", icon: "🤖" },
  { title: "CRM", href: "/dashboard/crm", icon: "👥" },
  { title: "Projects", href: "/dashboard/projects", icon: "📁" },
  { title: "Telegram", href: "/dashboard/telegram", icon: "💬" },
  { title: "Analytics", href: "/dashboard/analytics", icon: "📊" },
  { title: "Billing", href: "/dashboard/billing", icon: "💳" },
  { title: "Users", href: "/dashboard/users", icon: "👤" },
  { title: "Settings", href: "/dashboard/settings", icon: "⚙️" },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="sidebar">
      <div className="sidebar-logo">
        <span className="sidebar-logo-mark">N</span>

        <div>
          <h2>NOVA</h2>
          <small>Business OS</small>
        </div>
      </div>

      <nav className="sidebar-nav">
        {menu.map((item) => {
          const active =
            pathname === item.href ||
            pathname.startsWith(item.href + "/");

          return (
            <Link
              key={item.href}
              href={item.href}
              className={`sidebar-link ${active ? "active" : ""}`}
            >
              <span className="sidebar-icon">{item.icon}</span>

              <span>{item.title}</span>
            </Link>
          );
        })}
      </nav>

      <div className="sidebar-footer">
        <div className="workspace-card">
          <small>Workspace</small>

          <strong>NOVA Studio</strong>

          <span>Pro Plan</span>
        </div>

        <button className="logout-btn">
          🚪 Logout
        </button>
      </div>
    </aside>
  );
}
