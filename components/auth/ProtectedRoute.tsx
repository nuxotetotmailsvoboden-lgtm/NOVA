"use client";

import { ReactNode, useEffect } from "react";
import { useRouter } from "next/navigation";

import { useAuth } from "@/lib/hooks/useAuth";

interface ProtectedRouteProps {
  children: ReactNode;
}

export default function ProtectedRoute({
  children,
}: ProtectedRouteProps) {
  const router = useRouter();

  const {
    initialized,
    loading,
    isAuthenticated,
  } = useAuth();

  useEffect(() => {
    if (
      initialized &&
      !loading &&
      !isAuthenticated
    ) {
      router.replace("/login");
    }
  }, [
    initialized,
    loading,
    isAuthenticated,
    router,
  ]);

  if (!initialized || loading) {
    return (
      <div className="auth-loading">
        Загрузка...
      </div>
    );
  }

  if (!isAuthenticated) {
    return null;
  }

  return <>{children}</>;
}
