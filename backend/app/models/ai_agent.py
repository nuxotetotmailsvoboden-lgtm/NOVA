from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Index,
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class AIProvider(str, enum.Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    MISTRAL = "mistral"
    GROQ = "groq"
    OLLAMA = "ollama"
    OPENROUTER = "openrouter"
    CUSTOM = "custom"


class AIAgentStatus(str, enum.Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    DRAFT = "draft"


class AIAgent(BaseModel):
    __tablename__ = "ai_agents"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    created_by_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    provider: Mapped[AIProvider] = mapped_column(
        Enum(AIProvider),
        nullable=False,
        index=True,
    )

    model: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    system_prompt: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    tools: Mapped[list] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )

    settings: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    temperature: Mapped[float] = mapped_column(
        default=0.7,
        nullable=False,
    )

    max_tokens: Mapped[int] = mapped_column(
        Integer,
        default=4096,
        nullable=False,
    )

    status: Mapped[AIAgentStatus] = mapped_column(
        Enum(AIAgentStatus),
        default=AIAgentStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    is_system: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    created_by: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_ai_agent_workspace_status",
    AIAgent.workspace_id,
    AIAgent.status,
)

Index(
    "ix_ai_agent_workspace_provider",
    AIAgent.workspace_id,
    AIAgent.provider,
)

Index(
    "ix_ai_agent_workspace_model",
    AIAgent.workspace_id,
    AIAgent.model,
)
