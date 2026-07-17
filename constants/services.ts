export interface Service {
  id: string;
  title: string;
  description: string;
  price: number;
  icon: string;
}

export const SERVICES: Service[] = [
  {
    id: "miniapp",
    title: "Telegram Mini App",
    description: "Полноценное веб-приложение внутри Telegram.",
    price: 250000,
    icon: "🚀",
  },
  {
    id: "bot",
    title: "Telegram Bot",
    description: "Автоматизация бизнеса и продаж.",
    price: 100000,
    icon: "🤖",
  },
  {
    id: "crm",
    title: "CRM",
    description: "Учет клиентов, заявок и продаж.",
    price: 180000,
    icon: "📊",
  },
  {
    id: "ai",
    title: "AI Assistant",
    description: "ИИ-консультант для клиентов.",
    price: 200000,
    icon: "🧠",
  },
  {
    id: "payments",
    title: "Онлайн-оплата",
    description: "Kaspi, Stripe и другие платежи.",
    price: 70000,
    icon: "💳",
  },
];
