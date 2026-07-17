"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";

import { useAuth } from "@/lib/hooks/useAuth";

export default function LoginForm() {
  const router = useRouter();
  const { login, loading } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();

    setError("");

    try {
      await login({
        email,
        password,
      });

      router.replace("/dashboard");
    } catch {
      setError("Неверный email или пароль.");
    }
  }

  return (
    <form onSubmit={handleSubmit} className="login-form">
      <label>
        <span>Email</span>

        <input
          type="email"
          autoComplete="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="you@example.com"
          required
        />
      </label>

      <label>
        <span>Пароль</span>

        <input
          type="password"
          autoComplete="current-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="••••••••"
          required
        />
      </label>

      {error && (
        <div className="auth-error">
          {error}
        </div>
      )}

      <button
        type="submit"
        className="auth-submit"
        disabled={loading}
      >
        {loading ? "Вход..." : "Войти"}
      </button>
    </form>
  );
}
