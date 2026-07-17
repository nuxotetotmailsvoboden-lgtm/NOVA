export interface Project {
  id: number;
  title: string;
  category: string;
  description: string;
  tags: string[];
}

export const PROJECTS: Project[] = [
  {
    id: 1,
    title: "Telegram CRM",
    category: "Business",
    description: "CRM-система для управления клиентами, заявками и продажами.",
    tags: ["CRM", "Telegram", "Dashboard"],
  },
  {
    id: 2,
    title: "Flower Bot",
    category: "Automation",
    description: "Автоматизация приема заказов цветочного магазина.",
    tags: ["Bot", "Payments", "Mini App"],
  },
  {
    id: 3,
    title: "AI Assistant",
    category: "Artificial Intelligence",
    description: "ИИ-консультант с GPT для поддержки клиентов.",
    tags: ["AI", "GPT", "Support"],
  },
  {
    id: 4,
    title: "Crypto Dashboard",
    category: "Finance",
    description: "Панель мониторинга рынка и торговых сигналов.",
    tags: ["Crypto", "Analytics", "Charts"],
  },
  {
    id: 5,
    title: "Restaurant Mini App",
    category: "Food",
    description: "Заказы, бронирование столиков и онлайн-оплата.",
    tags: ["Mini App", "QR", "Kaspi"],
  },
  {
    id: 6,
    title: "Fitness Platform",
    category: "Health",
    description: "Абонементы, расписание и личный кабинет клиента.",
    tags: ["CRM", "Subscriptions", "Telegram"],
  },
];
