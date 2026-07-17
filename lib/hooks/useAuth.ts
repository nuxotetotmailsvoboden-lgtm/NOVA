"use client";

import { useEffect } from "react";

import { useAuthStore } from "@/lib/stores/auth.store";

export function useAuth() {
  const store = useAuthStore();

  useEffect(() => {
    if (!store.initialized) {
      store.initialize();
    }
  }, [store]);

  return {
    user: store.user,

    loading: store.loading,

    initialized: store.initialized,

    isAuthenticated: store.isAuthenticated,

    login: store.login,

    logout: store.logout,

    setUser: store.setUser,
  };
}
