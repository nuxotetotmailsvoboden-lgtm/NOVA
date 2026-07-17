from __future__ import annotations

import enum
import uuid
from decimal import Decimal

from sqlalchemy import (
    Enum,
    ForeignKey,
    Index,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class DealStage(str, enum.Enum):
    NEW = "new"
    CONTACT = "contact"
    QUALIFIED = "qualified"
    PROPOSAL = "proposal"
    NEGOTIATION = "negotiation"
    WON = "won"
    LOST = "lost"


class DealPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Deal(BaseModel):
    __tablename__ = "deals"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    manager_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        default=0,
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="KZT",
        nullable=False,
    )

    probability: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    priority: Mapped[DealPriority] = mapped_column(
        Enum(DealPriority),
        default=DealPriority.MEDIUM,
        nullable=False,
        index=True,
    )

    stage: Mapped[DealStage] = mapped_column(
        Enum(DealStage),
        default=DealStage.NEW,
        nullable=False,
        index=True,
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    client: Mapped["Client"] = relationship(
        "Client",
        lazy="joined",
    )

    manager: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_deal_workspace_stage",
    Deal.workspace_id,
    Deal.stage,
)

Index(
    "ix_deal_workspace_manager",
    Deal.workspace_id,
    Deal.manager_id,
)

Index(
    "ix_deal_workspace_client",
    Deal.workspace_id,
    Deal.client_id,
)
