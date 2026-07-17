"use client";

export default function Topbar() {
  return (
    <header className="topbar">
      <div className="topbar-left">
        <div className="search-box">
          <span className="search-icon">🔍</span>

          <input
            type="text"
            placeholder="Поиск по проектам, клиентам, задачам..."
          />
        </div>
      </div>

      <div className="topbar-right">

        <button className="topbar-action" title="Уведомления">
          🔔
        </button>

        <button className="topbar-action" title="Быстрые действия">
          ⚡
        </button>

        <button className="topbar-action" title="Переключить тему">
          🌙
        </button>

        <div className="topbar-user">

          <div className="user-avatar">
            N
          </div>

          <div className="user-info">
            <strong>NOVA Admin</strong>
            <small>Administrator</small>
          </div>

        </div>
      </div>
    </header>
  );
}
