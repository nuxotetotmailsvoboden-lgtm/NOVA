import { api } from "../api/client";
import {
  clearTokens,
  getAccessToken,
  getRefreshToken,
  setAccessToken,
  setRefreshToken,
} from "./token";

export interface LoginRequest {
  email: string;
  password: string;
}

export interface AuthUser {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  role: "admin" | "manager" | "user";
}

export interface AuthResponse {
  accessToken: string;
  refreshToken: string;
  user: AuthUser;
}

export async function login(
  payload: LoginRequest
): Promise<AuthUser> {
  const response = await api.post<AuthResponse>(
    "/auth/login",
    payload
  );

  setAccessToken(response.accessToken);
  setRefreshToken(response.refreshToken);

  return response.user;
}

export async function logout() {
  try {
    if (getRefreshToken()) {
      await api.post("/auth/logout", {
        refreshToken: getRefreshToken(),
      });
    }
  } finally {
    clearTokens();
  }
}

export async function refreshAccessToken(): Promise<string | null> {
  const refreshToken = getRefreshToken();

  if (!refreshToken) {
    clearTokens();
    return null;
  }

  try {
    const response = await api.post<{
      accessToken: string;
    }>("/auth/refresh", {
      refreshToken,
    });

    setAccessToken(response.accessToken);

    return response.accessToken;
  } catch {
    clearTokens();
    return null;
  }
}

export function hasSession() {
  return Boolean(getAccessToken());
}
