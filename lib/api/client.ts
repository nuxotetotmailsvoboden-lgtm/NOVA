import { getAccessToken } from "@/lib/auth/token";
import { refreshAccessToken } from "@/lib/auth/auth";

export interface ApiOptions extends RequestInit {
  params?: Record<string, string | number | boolean | undefined>;
}

const API_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api";

function buildUrl(
  path: string,
  params?: ApiOptions["params"]
) {
  const url = new URL(path, API_URL);

  if (params) {
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined) {
        url.searchParams.set(key, String(value));
      }
    });
  }

  return url.toString();
}

async function send<T>(
  path: string,
  options: ApiOptions,
  retry = true
): Promise<T> {
  const { params, headers, ...init } = options;

  const token = getAccessToken();

  const response = await fetch(buildUrl(path, params), {
    ...init,
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...(token
        ? {
            Authorization: `Bearer ${token}`,
          }
        : {}),
      ...headers,
    },
  });

  if (response.status === 401 && retry) {
    const newToken = await refreshAccessToken();

    if (newToken) {
      return send<T>(path, options, false);
    }
  }

  if (!response.ok) {
    const message = await response.text();

    throw new Error(message || `HTTP ${response.status}`);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json();
}

export const api = {
  get: <T>(
    path: string,
    params?: ApiOptions["params"]
  ) =>
    send<T>(
      path,
      {
        method: "GET",
        params,
      }
    ),

  post: <T>(
    path: string,
    body?: unknown
  ) =>
    send<T>(
      path,
      {
        method: "POST",
        body: JSON.stringify(body),
      }
    ),

  put: <T>(
    path: string,
    body?: unknown
  ) =>
    send<T>(
      path,
      {
        method: "PUT",
        body: JSON.stringify(body),
      }
    ),

  patch: <T>(
    path: string,
    body?: unknown
  ) =>
    send<T>(
      path,
      {
        method: "PATCH",
        body: JSON.stringify(body),
      }
    ),

  delete: <T>(path: string) =>
    send<T>(
      path,
      {
        method: "DELETE",
      }
    ),
};
