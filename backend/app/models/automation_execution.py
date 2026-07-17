from __future__ import annotations

import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Index,
    JSON,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class AutomationExecutionStatus(str, enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"


class AutomationExecution(BaseModel):
    __tablename__ = "automation_executions"

    automation_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("automations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    triggered_by_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    status: Mapped[AutomationExecutionStatus] = mapped_column(
        Enum(AutomationExecutionStatus),
        default=AutomationExecutionStatus.PENDING,
        nullable=False,
        index=True,
    )

    trigger_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    input_data: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    output_data: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    execution_time_ms: Mapped[float | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    automation: Mapped["Automation"] = relationship(
        "Automation",
        lazy="joined",
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    triggered_by: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_automation_execution_workspace",
    AutomationExecution.workspace_id,
)

Index(
    "ix_automation_execution_status",
    AutomationExecution.status,
)

Index(
    "ix_automation_execution_started",
    AutomationExecution.started_at,
)

Index(
    "ix_automation_execution_automation",
    AutomationExecution.automation_id,
)
