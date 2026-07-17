import type { AuthUser } from "./auth";

export type Role =
  | "admin"
  | "manager"
  | "employee"
  | "client";

export function isAuthenticated(
  user: AuthUser | null | undefined
): user is AuthUser {
  return user !== null && user !== undefined;
}

export function hasRole(
  user: AuthUser | null | undefined,
  role: Role
): boolean {
  if (!user) return false;

  return user.role === role;
}

export function hasAnyRole(
  user: AuthUser | null | undefined,
  roles: Role[]
): boolean {
  if (!user) return false;

  return roles.includes(user.role);
}

export function requireAuth(
  user: AuthUser | null | undefined
): asserts user is AuthUser {
  if (!user) {
    throw new Error("Authentication required.");
  }
}

export function requireGuest(
  user: AuthUser | null | undefined
): void {
  if (user) {
    throw new Error("Guest access only.");
  }
}

export function canAccess(
  user: AuthUser | null | undefined,
  allowedRoles: Role[]
): boolean {
  return hasAnyRole(user, allowedRoles);
}
