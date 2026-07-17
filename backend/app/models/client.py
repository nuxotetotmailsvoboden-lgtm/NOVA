from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Index,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class ClientStatus(str, enum.Enum):
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    NEGOTIATION = "negotiation"
    CUSTOMER = "customer"
    LOST = "lost"


class ClientSource(str, enum.Enum):
    WEBSITE = "website"
    TELEGRAM = "telegram"
    INSTAGRAM = "instagram"
    WHATSAPP = "whatsapp"
    FACEBOOK = "facebook"
    GOOGLE = "google"
    MANUAL = "manual"
    API = "api"
    OTHER = "other"


class Client(BaseModel):
    __tablename__ = "clients"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    manager_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    last_name: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
    )

    company: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    job_title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        index=True,
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        index=True,
        nullable=True,
    )

    telegram_username: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[ClientStatus] = mapped_column(
        Enum(ClientStatus),
        default=ClientStatus.NEW,
        nullable=False,
        index=True,
    )

    source: Mapped[ClientSource] = mapped_column(
        Enum(ClientSource),
        default=ClientSource.MANUAL,
        nullable=False,
        index=True,
    )

    is_company: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    manager: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_client_workspace_status",
    Client.workspace_id,
    Client.status,
)

Index(
    "ix_client_workspace_manager",
    Client.workspace_id,
    Client.manager_id,
)
