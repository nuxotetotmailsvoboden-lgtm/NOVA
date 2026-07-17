"use client";

import Container from "../ui/Container";

export default function DashboardPreview() {
  return (
    <section className="dashboard-preview">

      <Container>

        <div className="dashboard-header">

          <span>DASHBOARD</span>

          <h2>
            Управляйте бизнесом
            <br />
            из одного места
          </h2>

          <p>
            CRM, Telegram, AI, аналитика, продажи и автоматизация
            объединены в единую платформу NOVA.
          </p>

        </div>

        <div className="dashboard-window">

          <aside className="dashboard-sidebar">

            <div className="dashboard-logo">
              NOVA
            </div>

            <nav>

              <div className="sidebar-item active">
                📊 Dashboard
              </div>

              <div className="sidebar-item">
                🤖 AI
              </div>

              <div className="sidebar-item">
                👥 CRM
              </div>

              <div className="sidebar-item">
                💰 Sales
              </div>

              <div className="sidebar-item">
                📈 Analytics
              </div>

              <div className="sidebar-item">
                ⚙ Settings
              </div>

            </nav>

          </aside>

          <main className="dashboard-content">

            <div className="dashboard-cards">

              <div className="stat-card">

                <small>Revenue</small>

                <strong>$24,920</strong>

              </div>

              <div className="stat-card">

                <small>Projects</small>

                <strong>128</strong>

              </div>

              <div className="stat-card">

                <small>Clients</small>

                <strong>94</strong>

              </div>

              <div className="stat-card">

                <small>AI Tasks</small>

                <strong>18 291</strong>

              </div>

            </div>

            <div className="dashboard-chart">

              <div className="chart-line"></div>

            </div>

            <div className="dashboard-bottom">

              <div className="activity-card">

                <h3>Последняя активность</h3>

                <ul>

                  <li>✅ Новый заказ Telegram Mini App</li>

                  <li>🤖 AI обработал 125 запросов</li>

                  <li>💰 Получен платеж</li>

                  <li>📊 CRM обновлена</li>

                </ul>

              </div>

              <div className="ai-card">

                <h3>NOVA AI</h3>

                <p>
                  Добро пожаловать.
                  Чем могу помочь сегодня?
                </p>

              </div>

            </div>

          </main>

        </div>

      </Container>

    </section>
  );
}
