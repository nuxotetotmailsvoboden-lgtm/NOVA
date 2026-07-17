"use client";

import Container from "../ui/Container";
import Card from "../ui/Card";
import Button from "../ui/Button";

import { PROJECTS } from "@/constants/projects";

export default function Portfolio() {
  return (
    <section className="portfolio">
      <Container>

        <div className="portfolio-heading">
          <span>PORTFOLIO</span>

          <h2>Последние проекты</h2>

          <p>
            Примеры решений, которые помогают компаниям
            автоматизировать процессы и увеличивать прибыль.
          </p>
        </div>

        <div className="portfolio-grid">

          {PROJECTS.map(project => (

            <Card
              key={project.id}
              className="portfolio-card"
            >

              <div className="portfolio-preview" />

              <h3>{project.title}</h3>

              <small>{project.category}</small>

              <p>{project.description}</p>

              <div className="portfolio-tags">

                {project.tags.map(tag => (

                  <span key={tag}>
                    {tag}
                  </span>

                ))}

              </div>

              <Button>
                Подробнее
              </Button>

            </Card>

          ))}

        </div>

      </Container>
    </section>
  );
}
