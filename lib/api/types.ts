/* ============
   COMMON
============ */

export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
}

/* ============
   USER
============ */

export interface User {
  id: string;

  firstName: string;

  lastName: string;

  email: string;

  avatar?: string;

  role: "admin" | "manager" | "user";

  createdAt: string;

  updatedAt: string;
}

/* ============
   CLIENT
============ */

export interface Client {
  id: string;

  company: string;

  contactName: string;

  email: string;

  phone: string;

  status:
    | "new"
    | "lead"
    | "negotiation"
    | "active"
    | "closed";

  value: number;

  notes?: string;

  createdAt: string;

  updatedAt: string;
}

/* ============
   PROJECT
============ */

export interface Project {
  id: string;

  clientId: string;

  title: string;

  description?: string;

  status:
    | "planning"
    | "development"
    | "testing"
    | "completed";

  progress: number;

  budget: number;

  deadline?: string;

  createdAt: string;
}

/* ============
   DEAL
============ */

export interface Deal {
  id: string;

  clientId: string;

  amount: number;

  stage:
    | "lead"
    | "proposal"
    | "negotiation"
    | "won"
    | "lost";

  createdAt: string;
}

/* ============
   TASK
============ */

export interface Task {
  id: string;

  title: string;

  description?: string;

  completed: boolean;

  dueDate?: string;

  assigneeId?: string;
}

/* ============
   NOTIFICATION
============ */

export interface Notification {
  id: string;

  title: string;

  message: string;

  read: boolean;

  createdAt: string;
}

/* ============
   AI CHAT
============ */

export interface AIChatMessage {
  id: string;

  role: "user" | "assistant";

  content: string;

  createdAt: string;
}

/* ============
   ANALYTICS
============ */

export interface AnalyticsSummary {
  revenue: number;

  clients: number;

  projects: number;

  conversions: number;

  aiRequests: number;
}
