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
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class AIMessageRole(str, enum.Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class AIMessageStatus(str, enum.Enum):
    PENDING = "pending"
    STREAMING = "streaming"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class AIMessage(BaseModel):
    __tablename__ = "ai_messages"

    conversation_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ai_conversations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    author_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    role: Mapped[AIMessageRole] = mapped_column(
        Enum(AIMessageRole),
        nullable=False,
        index=True,
    )

    status: Mapped[AIMessageStatus] = mapped_column(
        Enum(AIMessageStatus),
        default=AIMessageStatus.PENDING,
        nullable=False,
        index=True,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    tool_calls: Mapped[list] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )

    tool_results: Mapped[list] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )

    metadata: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    prompt_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    completion_tokens: Mapped[int] = mapped_column(
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

    generation_time_ms: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    is_edited: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    conversation: Mapped["AIConversation"] = relationship(
        "AIConversation",
        lazy="joined",
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    author: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_ai_message_conversation",
    AIMessage.conversation_id,
)

Index(
    "ix_ai_message_workspace_role",
    AIMessage.workspace_id,
    AIMessage.role,
)

Index(
    "ix_ai_message_workspace_status",
    AIMessage.workspace_id,
    AIMessage.status,
)
