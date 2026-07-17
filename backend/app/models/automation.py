from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Index,
    JSON,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class AutomationStatus(str, enum.Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    DRAFT = "draft"


class AutomationTrigger(str, enum.Enum):
    CLIENT_CREATED = "client_created"
    CLIENT_UPDATED = "client_updated"

    DEAL_CREATED = "deal_created"
    DEAL_UPDATED = "deal_updated"
    DEAL_STAGE_CHANGED = "deal_stage_changed"
    DEAL_WON = "deal_won"
    DEAL_LOST = "deal_lost"

    TASK_CREATED = "task_created"
    TASK_COMPLETED = "task_completed"
    TASK_OVERDUE = "task_overdue"

    NOTE_CREATED = "note_created"
    FILE_UPLOADED = "file_uploaded"

    USER_REGISTERED = "user_registered"
    SCHEDULE = "schedule"
    WEBHOOK = "webhook"
    API = "api"


class Automation(BaseModel):
    __tablename__ = "automations"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    created_by_id: Mapped[uuid.UUID] = mapped_column(
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

    trigger: Mapped[AutomationTrigger] = mapped_column(
        Enum(AutomationTrigger),
        nullable=False,
        index=True,
    )

    status: Mapped[AutomationStatus] = mapped_column(
        Enum(AutomationStatus),
        default=AutomationStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    conditions: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    actions: Mapped[list] = mapped_column(
        JSON,
        default=list,
        nullable=False,
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
    "ix_automation_workspace_status",
    Automation.workspace_id,
    Automation.status,
)

Index(
    "ix_automation_workspace_trigger",
    Automation.workspace_id,
    Automation.trigger,
)
