"use client";

import Card from "../ui/Card";
import Container from "../ui/Container";
import Button from "../ui/Button";

import { SERVICES } from "@/constants/services";
import { formatPrice } from "@/utils/formatPrice";

export default function Services() {
    return (
        <section className="services">

            <Container>

                <div className="services-heading">

                    <span className="services-subtitle">
                        SERVICES
                    </span>

                    <h2>
                        Что мы создаем
                    </h2>

                    <p>
                        Разрабатываем современные цифровые продукты
                        для бизнеса любого масштаба.
                    </p>

                </div>

                <div className="services-grid">

                    {SERVICES.map(service => (

                        <Card
                            key={service.id}
                            className="service-card"
                        >

                            <div className="service-icon">
                                {service.icon}
                            </div>

                            <h3>
                                {service.title}
                            </h3>

                            <p>
                                {service.description}
                            </p>

                            <div className="service-bottom">

                                <strong>
                                    {formatPrice(service.price)}
                                </strong>

                                <Button>
                                    Подробнее
                                </Button>

                            </div>

                        </Card>

                    ))}

                </div>

            </Container>

        </section>
    );
}
