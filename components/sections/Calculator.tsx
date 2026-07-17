"use client";

import { useMemo, useState } from "react";

import Container from "../ui/Container";
import Card from "../ui/Card";
import Button from "../ui/Button";

const BASE_PRICE = 100000;

export default function Calculator() {
  const [pages, setPages] = useState(5);
  const [telegramBot, setTelegramBot] = useState(true);
  const [miniApp, setMiniApp] = useState(false);
  const [crm, setCrm] = useState(false);
  const [ai, setAi] = useState(false);

  const total = useMemo(() => {
    let price = BASE_PRICE;

    price += pages * 10000;

    if (telegramBot) price += 100000;
    if (miniApp) price += 250000;
    if (crm) price += 180000;
    if (ai) price += 200000;

    return price;
  }, [pages, telegramBot, miniApp, crm, ai]);

  return (
    <section className="calculator">
      <Container>
        <div className="calculator-header">
          <span>CALCULATOR</span>

          <h2>Рассчитайте стоимость проекта</h2>

          <p>
            Выберите необходимые функции и получите ориентировочную стоимость.
          </p>
        </div>

        <div className="calculator-grid">
          <Card>
            <div className="calc-group">
              <label>Количество экранов</label>

              <input
                type="range"
                min={1}
                max={30}
                value={pages}
                onChange={(e) => setPages(Number(e.target.value))}
              />

              <strong>{pages} экранов</strong>
            </div>

            <div className="calc-switch">
              <label>
                <input
                  type="checkbox"
                  checked={telegramBot}
                  onChange={() => setTelegramBot(!telegramBot)}
                />
                Telegram Bot
              </label>

              <label>
                <input
                  type="checkbox"
                  checked={miniApp}
                  onChange={() => setMiniApp(!miniApp)}
                />
                Telegram Mini App
              </label>

              <label>
                <input
                  type="checkbox"
                  checked={crm}
                  onChange={() => setCrm(!crm)}
                />
                CRM
              </label>

              <label>
                <input
                  type="checkbox"
                  checked={ai}
                  onChange={() => setAi(!ai)}
                />
                AI Assistant
              </label>
            </div>
          </Card>

          <Card className="calculator-result">
            <span>Итоговая стоимость</span>

            <h2>{total.toLocaleString("ru-RU")} ₸</h2>

            <Button>
              Обсудить проект
            </Button>
          </Card>
        </div>
      </Container>
    </section>
  );
}
