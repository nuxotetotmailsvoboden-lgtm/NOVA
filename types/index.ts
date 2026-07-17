export interface User {
  id: number;
  telegramId: number;
  username: string;
  firstName: string;
  lastName?: string;
  avatar?: string;
  language: string;
  isAdmin: boolean;
  createdAt: string;
}

export interface Project {
  id: number;
  title: string;
  description: string;
  price: number;
  status: string;
}

export interface Review {
  id: number;
  name: string;
  avatar: string;
  rating: number;
  text: string;
}
