"use client";

interface ClientDetailsProps {
  client?: {
    id: number;
    name: string;
    company: string;
    email: string;
    phone: string;
    status: string;
    value: string;
  };
}

const demoClient = {
  id: 1,
  name: "Алексей Иванов",
  company: "TechVision",
  email: "alexey@techvision.io",
  phone: "+7 (777) 123-45-67",
  status: "Активный",
  value: "$12,500",
};

export default function ClientDetails({
  client = demoClient,
}: ClientDetailsProps) {
  return (
    <div className="client-details">

      <div className="client-card">

        <div className="client-avatar">
          {client.company.charAt(0)}
        </div>

        <div className="client-main">

          <h2>{client.company}</h2>

          <p>{client.name}</p>

          <span className="client-status">
            {client.status}
          </span>

        </div>

        <div className="client-value">

          <small>Сумма сделки</small>

          <strong>{client.value}</strong>

        </div>

      </div>

      <div className="client-grid">

        <section className="client-panel">

          <h3>Контактная информация</h3>

          <div className="info-row">
            <span>Email</span>
            <strong>{client.email}</strong>
          </div>

          <div className="info-row">
            <span>Телефон</span>
            <strong>{client.phone}</strong>
          </div>

          <div className="info-row">
            <span>Компания</span>
            <strong>{client.company}</strong>
          </div>

        </section>

        <section className="client-panel">

          <h3>Последние задачи</h3>

          <ul className="task-list">
            <li>✅ Отправить коммерческое предложение</li>
            <li>📞 Созвониться во вторник</li>
            <li>💬 Ответить в Telegram</li>
            <li>📄 Подготовить договор</li>
          </ul>

        </section>

      </div>

      <div className="client-grid">

        <section className="client-panel">

          <h3>Последние сообщения</h3>

          <div className="message">
            <strong>Клиент</strong>
            <p>Интересует Telegram Mini App для интернет-магазина.</p>
          </div>

          <div className="message own">
            <strong>Менеджер</strong>
            <p>Подготовили предложение. Отправим сегодня до 18:00.</p>
          </div>

        </section>

        <section className="client-panel">

          <h3>AI Рекомендации</h3>

          <div className="ai-tip">
            💡 Вероятность закрытия сделки — <strong>82%</strong>.
          </div>

          <div className="ai-tip">
            📈 Рекомендуется назначить демонстрацию продукта в течение 48 часов.
          </div>

          <div className="ai-tip">
            🤖 Следующее оптимальное действие — отправить коммерческое предложение.
          </div>

        </section>

      </div>

    </div>
  );
}
