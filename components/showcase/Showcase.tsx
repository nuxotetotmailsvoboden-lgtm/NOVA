"use client";

import Container from "../ui/Container";
import Laptop from "./Laptop";
import Phone from "./Phone";

export default function Showcase() {
  return (
    <section className="showcase">

      <Container>

        <div className="showcase-header">

          <span>SHOWCASE</span>

          <h2>
            Всё в одном продукте
          </h2>

          <p>
            Telegram Mini Apps, CRM, AI и автоматизация —
            единая экосистема NOVA.
          </p>

        </div>

        <div className="showcase-scene">

          <Laptop />

          <Phone />

        </div>

      </Container>

    </section>
  );
}
