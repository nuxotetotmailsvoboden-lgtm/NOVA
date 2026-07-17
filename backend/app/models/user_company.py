from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Enum,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class CompanyRole(str, enum.Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MANAGER = "manager"
    EMPLOYEE = "employee"


class UserCompany(BaseModel):
    """
    Связь пользователя с компанией.

    Один пользователь может состоять в нескольких компаниях.
    Одна компания может иметь множество пользователей.
    """

    __tablename__ = "user_companies"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "company_id",
            name="uq_user_company",
        ),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    company_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    role: Mapped[CompanyRole] = mapped_column(
        Enum(CompanyRole),
        default=CompanyRole.EMPLOYEE,
        nullable=False,
        index=True,
    )

    is_default: Mapped[bool] = mapped_column(
        default=False,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
        index=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        lazy="joined",
    )

    company: Mapped["Company"] = relationship(
        "Company",
        lazy="joined",
    )
