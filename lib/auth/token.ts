const ACCESS_TOKEN_KEY = "nova_access_token";
const REFRESH_TOKEN_KEY = "nova_refresh_token";

export function getAccessToken(): string | null {
  if (typeof window === "undefined") return null;

  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

export function setAccessToken(token: string) {
  if (typeof window === "undefined") return;

  localStorage.setItem(ACCESS_TOKEN_KEY, token);
}

export function removeAccessToken() {
  if (typeof window === "undefined") return;

  localStorage.removeItem(ACCESS_TOKEN_KEY);
}

export function getRefreshToken(): string | null {
  if (typeof window === "undefined") return null;

  return localStorage.getItem(REFRESH_TOKEN_KEY);
}

export function setRefreshToken(token: string) {
  if (typeof window === "undefined") return;

  localStorage.setItem(REFRESH_TOKEN_KEY, token);
}

export function removeRefreshToken() {
  if (typeof window === "undefined") return;

  localStorage.removeItem(REFRESH_TOKEN_KEY);
}

export function clearTokens() {
  removeAccessToken();
  removeRefreshToken();
}

export function isAuthenticated() {
  return !!getAccessToken();
}
