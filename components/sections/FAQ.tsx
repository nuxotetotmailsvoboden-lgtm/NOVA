"use client";

import { useState } from "react";

import Container from "../ui/Container";

const FAQ_ITEMS = [
  {
    question: "Сколько занимает разработка проекта?",
    answer:
      "В среднем от 7 до 30 дней в зависимости от сложности, количества функций и интеграций.",
  },
  {
    question: "Вы разрабатываете Telegram Mini Apps?",
    answer:
      "Да. Мы создаем полноценные Mini Apps с современным интерфейсом, CRM, оплатой, авторизацией и интеграциями.",
  },
  {
    question: "Можно подключить Kaspi и другие платежи?",
    answer:
      "Да. Подключаем платежные системы, CRM, Telegram Bot API, AI и любые необходимые сервисы.",
  },
  {
    question: "После запуска есть поддержка?",
    answer:
      "Да. Мы сопровождаем проекты, обновляем функциональность и обеспечиваем техническую поддержку.",
  },
];

export default function FAQ() {
  const [active, setActive] = useState<number | null>(0);

  return (
    <section className="faq">
      <Container>
        <div className="faq-header">
          <span>FAQ</span>

          <h2>Частые вопросы</h2>

          <p>
            Ответы на самые популярные вопросы наших клиентов.
          </p>
        </div>

        <div className="faq-list">
          {FAQ_ITEMS.map((item, index) => {
            const opened = active === index;

            return (
              <div
                key={index}
                className={`faq-item ${opened ? "active" : ""}`}
                onClick={() =>
                  setActive(opened ? null : index)
                }
              >
                <div className="faq-question">
                  <h3>{item.question}</h3>

                  <span className="faq-icon">
                    {opened ? "−" : "+"}
                  </span>
                </div>

                <div
                  className={`faq-answer ${
                    opened ? "show" : ""
                  }`}
                >
                  <p>{item.answer}</p>
                </div>
              </div>
            );
          })}
        </div>
      </Container>
    </section>
  );
}
