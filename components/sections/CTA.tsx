"use client";

import Container from "../ui/Container";
import Button from "../ui/Button";

export default function CTA() {
  return (
    <section className="cta">
      <Container>

        <div className="cta-box">

          <span className="cta-badge">
            🚀 START YOUR PROJECT
          </span>

          <h2>
            Создадим ваш следующий
            <br />
            Telegram-продукт
          </h2>

          <p>
            Telegram Mini Apps, CRM, AI-ассистенты,
            автоматизация бизнеса, платежи и аналитика —
            всё в одном решении.
          </p>

          <div className="cta-buttons">

            <Button>
              🚀 Заказать проект
            </Button>

            <Button variant="secondary">
              💬 Telegram
            </Button>

          </div>

          <div className="cta-stats">

            <div>
              <strong>100+</strong>
              <span>Проектов</span>
            </div>

            <div>
              <strong>24/7</strong>
              <span>Поддержка</span>
            </div>

            <div>
              <strong>99%</strong>
              <span>Довольных клиентов</span>
            </div>

          </div>

        </div>

      </Container>
    </section>
  );
}
