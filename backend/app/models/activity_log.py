from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Enum,
    ForeignKey,
    Index,
    JSON,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class ActivityEntity(str, enum.Enum):
    USER = "user"
    COMPANY = "company"
    WORKSPACE = "workspace"
    CLIENT = "client"
    DEAL = "deal"
    TASK = "task"
    NOTE = "note"
    ATTACHMENT = "attachment"
    TAG = "tag"
    AI = "ai"
    TELEGRAM = "telegram"
    SYSTEM = "system"


class ActivityAction(str, enum.Enum):
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"
    RESTORED = "restored"
    ASSIGNED = "assigned"
    COMPLETED = "completed"
    COMMENTED = "commented"
    UPLOADED = "uploaded"
    EXPORTED = "exported"
    LOGIN = "login"
    LOGOUT = "logout"
    EXECUTED = "executed"


class ActivityLog(BaseModel):
    __tablename__ = "activity_logs"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    user_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    entity_type: Mapped[ActivityEntity] = mapped_column(
        Enum(ActivityEntity),
        nullable=False,
        index=True,
    )

    entity_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
    )

    action: Mapped[ActivityAction] = mapped_column(
        Enum(ActivityAction),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    metadata: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    user: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_activity_workspace_entity",
    ActivityLog.workspace_id,
    ActivityLog.entity_type,
)

Index(
    "ix_activity_workspace_action",
    ActivityLog.workspace_id,
    ActivityLog.action,
)

Index(
    "ix_activity_workspace_user",
    ActivityLog.workspace_id,
    ActivityLog.user_id,
)

Index(
    "ix_activity_entity_lookup",
    ActivityLog.entity_type,
    ActivityLog.entity_id,
)
