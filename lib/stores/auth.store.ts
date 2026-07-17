import { create } from "zustand";

import {
  login,
  logout,
  type AuthUser,
} from "@/lib/auth/auth";

interface LoginData {
  email: string;
  password: string;
}

interface AuthStore {
  user: AuthUser | null;

  loading: boolean;

  initialized: boolean;

  isAuthenticated: boolean;

  setUser: (user: AuthUser | null) => void;

  initialize: () => Promise<void>;

  login: (data: LoginData) => Promise<void>;

  logout: () => Promise<void>;
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,

  loading: false,

  initialized: false,

  isAuthenticated: false,

  setUser(user) {
    set({
      user,
      isAuthenticated: !!user,
    });
  },

  async initialize() {
    set({ initialized: true });

    // Здесь позже будет запрос:
    // GET /auth/me
    // Пока оставляем заготовку.
  },

  async login(data) {
    set({
      loading: true,
    });

    try {
      const user = await login(data);

      set({
        user,
        isAuthenticated: true,
      });
    } finally {
      set({
        loading: false,
      });
    }
  },

  async logout() {
    set({
      loading: true,
    });

    try {
      await logout();
    } finally {
      set({
        user: null,
        isAuthenticated: false,
        loading: false,
      });
    }
  },
}));
