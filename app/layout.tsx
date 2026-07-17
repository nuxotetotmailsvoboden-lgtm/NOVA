import "./globals.css";

export const metadata = {
  title: "NOVA",
  description: "Premium Telegram Mini App Platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ru">
      <body>{children}</body>
    </html>
  );
}
