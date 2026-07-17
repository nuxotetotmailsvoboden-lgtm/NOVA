"use client";

import { NAVIGATION } from "@/constants/navigation";

export default function Menu() {
  return (
    <nav className="nova-menu">
      {NAVIGATION.map((item) => (
        <a
          key={item.id}
          href={item.href}
          className="nova-menu-item"
        >
          {item.title}
        </a>
      ))}
    </nav>
  );
}
