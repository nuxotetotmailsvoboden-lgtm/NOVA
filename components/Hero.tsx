"use client";

import Button from "./ui/Button";
import Badge from "./ui/Badge";
import Card from "./ui/Card";
import Container from "./ui/Container";

export default function Hero() {
  return (
    <section className="hero">

      <div className="hero-glow hero-glow-left"></div>
      <div className="hero-glow hero-glow-right"></div>

      <div className="hero-container">

        <Badge>🚀 Premium Telegram Platform</Badge>

        <h1 className="hero-title">
          Создаем Telegram-
          <br />
          продукты нового поколения
        </h1>

        <p className="hero-description">
          Mini Apps, Telegram-боты, CRM, AI-ассистенты,
          автоматизация бизнеса и индивидуальная разработка.
        </p>

        <div className="hero-actions">

          <Button>
            Создать проект
          </Button>

          <Button variant="secondary">
            Смотреть демо
          </Button>

        </div>

        <div className="hero-stats">

          <Card className="hero-stat">
            <h3>100+</h3>
            <span>Проектов</span>
          </Card>

          <Card className="hero-stat">
            <h3>24/7</h3>
            <span>Поддержка</span>
          </Card>

          <Card className="hero-stat">
            <h3>AI</h3>
            <span>Автоматизация</span>
          </Card>

        </div>

      </div>

    </section>
  );
}
