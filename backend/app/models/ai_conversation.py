from __future__ import annotations

import enum
import uuid
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Index,
    Integer,
    JSON,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class AIConversationStatus(str, enum.Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    CLOSED = "closed"


class AIConversation(BaseModel):
    __tablename__ = "ai_conversations"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    agent_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ai_agents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    user_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    context: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    model: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    provider: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    input_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    output_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    total_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    estimated_cost: Mapped[Decimal] = mapped_column(
        Numeric(12, 6),
        default=0,
        nullable=False,
    )

    status: Mapped[AIConversationStatus] = mapped_column(
        Enum(AIConversationStatus),
        default=AIConversationStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    pinned: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    agent: Mapped["AIAgent"] = relationship(
        "AIAgent",
        lazy="joined",
    )

    user: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_ai_conversation_workspace_status",
    AIConversation.workspace_id,
    AIConversation.status,
)

Index(
    "ix_ai_conversation_workspace_user",
    AIConversation.workspace_id,
    AIConversation.user_id,
)

Index(
    "ix_ai_conversation_workspace_agent",
    AIConversation.workspace_id,
    AIConversation.agent_id,
)
