"use client";

import Container from "../ui/Container";
import Card from "../ui/Card";

const REVIEWS = [
  {
    name: "Александр",
    company: "Retail",
    text: "Команда NOVA автоматизировала наш бизнес. Telegram теперь приносит заявки каждый день.",
    rating: 5,
  },
  {
    name: "Айгерим",
    company: "Beauty Studio",
    text: "Mini App получился невероятно удобным. Клиенты записываются сами, без менеджеров.",
    rating: 5,
  },
  {
    name: "Дмитрий",
    company: "Crypto",
    text: "Сделали CRM, AI и Telegram-бота. Экономим десятки часов каждую неделю.",
    rating: 5,
  },
];

export default function Reviews() {
  return (
    <section className="reviews">
      <Container>
        <div className="reviews-header">
          <span>REVIEWS</span>

          <h2>Что говорят клиенты</h2>

          <p>
            Компании выбирают NOVA для автоматизации процессов,
            создания Telegram Mini Apps и внедрения искусственного интеллекта.
          </p>
        </div>

        <div className="reviews-grid">
          {REVIEWS.map((review, index) => (
            <Card
              key={index}
              className="review-card"
            >
              <div className="review-stars">
                ⭐⭐⭐⭐⭐
              </div>

              <p className="review-text">
                {review.text}
              </p>

              <div className="review-author">
                <strong>{review.name}</strong>

                <span>{review.company}</span>
              </div>
            </Card>
          ))}
        </div>
      </Container>
    </section>
  );
}
