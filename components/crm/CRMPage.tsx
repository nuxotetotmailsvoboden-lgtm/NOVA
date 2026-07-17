"use client";

const clients = [
  {
    id: 1,
    name: "TechVision",
    contact: "Алексей Иванов",
    status: "Активный",
    value: "$12,500",
  },
  {
    id: 2,
    name: "Beauty Studio",
    contact: "Мария Смирнова",
    status: "Переговоры",
    value: "$4,800",
  },
  {
    id: 3,
    name: "Coffee House",
    contact: "Данияр Ахметов",
    status: "Новый",
    value: "$2,100",
  },
  {
    id: 4,
    name: "Logistics Pro",
    contact: "Игорь Петров",
    status: "Активный",
    value: "$18,300",
  },
];

export default function CRMPage() {
  return (
    <div className="crm-page">

      <div className="crm-header">

        <div>
          <h1>CRM</h1>
          <p>Управление клиентами и сделками</p>
        </div>

        <button className="crm-add-btn">
          + Новый клиент
        </button>

      </div>

      <div className="crm-toolbar">

        <input
          type="text"
          placeholder="Поиск клиента..."
          className="crm-search"
        />

        <select className="crm-filter">
          <option>Все статусы</option>
          <option>Активный</option>
          <option>Переговоры</option>
          <option>Новый</option>
        </select>

      </div>

      <div className="crm-table">

        <div className="crm-table-head">

          <span>Компания</span>
          <span>Контакт</span>
          <span>Статус</span>
          <span>Стоимость</span>
          <span></span>

        </div>

        {clients.map((client) => (
          <div className="crm-row" key={client.id}>

            <span>{client.name}</span>

            <span>{client.contact}</span>

            <span className={`crm-status ${client.status.toLowerCase()}`}>
              {client.status}
            </span>

            <strong>{client.value}</strong>

            <button className="crm-open-btn">
              Открыть
            </button>

          </div>
        ))}

      </div>

    </div>
  );
}
