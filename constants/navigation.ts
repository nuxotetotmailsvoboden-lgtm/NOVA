export interface NavItem {
  id: string;
  title: string;
  href: string;
}

export const NAVIGATION: NavItem[] = [
  {
    id: "home",
    title: "Главная",
    href: "/",
  },
  {
    id: "services",
    title: "Услуги",
    href: "/services",
  },
  {
    id: "builder",
    title: "Конструктор",
    href: "/builder",
  },
  {
    id: "portfolio",
    title: "Портфолио",
    href: "/portfolio",
  },
  {
    id: "pricing",
    title: "Цены",
    href: "/pricing",
  },
  {
    id: "reviews",
    title: "Отзывы",
    href: "/reviews",
  },
  {
    id: "faq",
    title: "FAQ",
    href: "/faq",
  },
  {
    id: "contacts",
    title: "Контакты",
    href: "/contacts",
  },
];
