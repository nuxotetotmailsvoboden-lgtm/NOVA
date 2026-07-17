"use client";

import Logo from "./Logo";
import Menu from "./Menu";
import Button from "./ui/Button";

export default function Navbar() {
  return (
    <header className="nova-navbar">

      <Logo />

      <Menu />

      <div className="nova-navbar-actions">
        <Button variant="ghost">
          Войти
        </Button>

        <Button>
          Создать проект
        </Button>
      </div>

    </header>
  );
}
