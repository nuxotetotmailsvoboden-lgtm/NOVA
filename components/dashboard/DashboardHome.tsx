"use client";

const stats = [
  {
    title: "Доход",
    value: "$24,920",
    change: "+18.4%",
  },
  {
    title: "Проекты",
    value: "128",
    change: "+6",
  },
  {
    title: "Клиенты",
    value: "94",
    change: "+12%",
  },
  {
    title: "AI запросы",
    value: "18,291",
    change: "+31%",
  },
];

const activities = [
  "Создан новый Telegram Mini App",
  "Оплачен счёт #2841",
  "AI завершил анализ проекта",
  "Добавлен новый клиент",
  "Обновлена CRM",
];

export default function DashboardHome() {
  return (
    <div className="dashboard-home">

      <section className="dashboard-stats">
        {stats.map((item) => (
          <article className="kpi-card" key={item.title}>
            <span>{item.title}</span>

            <strong>{item.value}</strong>

            <small>{item.change} за месяц</small>
          </article>
        ))}
      </section>

      <section className="dashboard-grid">

        <div className="dashboard-panel dashboard-chart-panel">
          <div className="panel-header">
            <h3>Обзор дохода</h3>
            <button>Сегодня</button>
          </div>

          <div className="fake-chart">
            <div className="chart-gradient" />
            <div className="chart-line" />
          </div>
        </div>

        <div className="dashboard-panel ai-widget">

          <div className="panel-header">
            <h3>NOVA AI</h3>
          </div>

          <div className="ai-message">
            👋 Добро пожаловать!
          </div>

          <div className="ai-message secondary">
            Сегодня открыто 8 проектов.
          </div>

          <div className="ai-message secondary">
            Есть 3 новых обращения клиентов.
          </div>

          <button className="ai-button">
            Открыть AI Assistant
          </button>

        </div>

      </section>

      <section className="dashboard-grid">

        <div className="dashboard-panel">

          <div className="panel-header">
            <h3>Последняя активность</h3>
          </div>

          <ul className="activity-list">
            {activities.map((item) => (
              <li key={item}>
                ✅ {item}
              </li>
            ))}
          </ul>

        </div>

        <div className="dashboard-panel">

          <div className="panel-header">
            <h3>Быстрые действия</h3>
          </div>

          <div className="quick-actions">

            <button>+ Новый проект</button>

            <button>+ Новый клиент</button>

            <button>🤖 Запустить AI</button>

            <button>📊 Аналитика</button>

          </div>

        </div>

      </section>

    </div>
  );
}
