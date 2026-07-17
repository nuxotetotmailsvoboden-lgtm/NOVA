import AuthLayout from "@/components/auth/AuthLayout";
import LoginForm from "@/components/auth/LoginForm";

export default function LoginPage() {
  return (
    <AuthLayout
      title="Добро пожаловать в NOVA"
      subtitle="Войдите в систему, чтобы продолжить работу."
    >
      <LoginForm />
    </AuthLayout>
  );
}
