import { z } from "zod";

export const loginSchema = z.object({
  email: z
    .email("Введите корректный email")
    .trim()
    .toLowerCase(),

  password: z
    .string()
    .min(8, "Пароль должен содержать минимум 8 символов")
    .max(128, "Пароль слишком длинный"),
});

export type LoginFormData = z.infer<typeof loginSchema>;

export function validateLogin(data: unknown) {
  return loginSchema.safeParse(data);
}
