from __future__ import annotations

from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class Company(BaseModel):
    """
    Компания (tenant).

    В будущем все сущности (CRM, сделки, боты, сотрудники,
    настройки и т.д.) будут привязаны к company_id.
    """

    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    slug: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    logo_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    timezone: Mapped[str] = mapped_column(
        String(64),
        default="Asia/Almaty",
        nullable=False,
    )

    language: Mapped[str] = mapped_column(
        String(10),
        default="ru",
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="KZT",
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )
