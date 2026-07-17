from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class WorkspaceType(str, enum.Enum):
    PERSONAL = "personal"
    TEAM = "team"
    BUSINESS = "business"


class Workspace(BaseModel):
    """
    Рабочее пространство NOVA.

    Именно внутри Workspace будут жить:

    • CRM
    • Telegram Bot
    • Telegram Mini App
    • AI Assistant
    • Analytics
    • Knowledge Base
    • Automation
    • Billing
    """

    __tablename__ = "workspaces"

    __table_args__ = (
        UniqueConstraint(
            "company_id",
            "slug",
            name="uq_workspace_slug",
        ),
    )

    company_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    owner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    avatar_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    workspace_type: Mapped[WorkspaceType] = mapped_column(
        Enum(WorkspaceType),
        default=WorkspaceType.BUSINESS,
        nullable=False,
    )

    color: Mapped[str] = mapped_column(
        String(20),
        default="#3B82F6",
        nullable=False,
    )

    icon: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )

    company: Mapped["Company"] = relationship(
        "Company",
        lazy="joined",
    )

    owner: Mapped["User"] = relationship(
        "User",
        lazy="joined",
    )
