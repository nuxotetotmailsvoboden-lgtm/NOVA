from __future__ import annotations

import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
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


class CalendarEventType(str, enum.Enum):
    MEETING = "meeting"
    CALL = "call"
    TASK = "task"
    DEADLINE = "deadline"
    REMINDER = "reminder"
    PERSONAL = "personal"
    SYSTEM = "system"


class CalendarEventStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    MISSED = "missed"


class CalendarEvent(BaseModel):
    __tablename__ = "calendar_events"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    creator_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    assignee_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    client_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    deal_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("deals.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    task_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id", ondelete="SET NULL"),
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

    event_type: Mapped[CalendarEventType] = mapped_column(
        Enum(CalendarEventType),
        nullable=False,
        index=True,
    )

    status: Mapped[CalendarEventStatus] = mapped_column(
        Enum(CalendarEventStatus),
        default=CalendarEventStatus.SCHEDULED,
        nullable=False,
        index=True,
    )

    starts_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    ends_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    timezone: Mapped[str] = mapped_column(
        String(64),
        default="UTC",
        nullable=False,
    )

    location: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    meeting_url: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
    )

    recurrence_rule: Mapped[str | None] = mapped_column(
        String(512),
        nullable=True,
    )

    attendees: Mapped[list] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )

    reminders: Mapped[list] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )

    is_all_day: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    color: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    external_provider: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    external_event_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    sync_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    metadata: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    workspace: Mapped["Workspace"] = relationship("Workspace", lazy="joined")
    creator: Mapped["User"] = relationship(
        "User",
        foreign_keys=[creator_id],
        lazy="joined",
    )
    assignee: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[assignee_id],
        lazy="joined",
    )
    client: Mapped["Client | None"] = relationship("Client", lazy="joined")
    deal: Mapped["Deal | None"] = relationship("Deal", lazy="joined")
    task: Mapped["Task | None"] = relationship("Task", lazy="joined")


Index(
    "ix_calendar_workspace_start",
    CalendarEvent.workspace_id,
    CalendarEvent.starts_at,
)

Index(
    "ix_calendar_workspace_assignee",
    CalendarEvent.workspace_id,
    CalendarEvent.assignee_id,
)

Index(
    "ix_calendar_workspace_status",
    CalendarEvent.workspace_id,
    CalendarEvent.status,
)

Index(
    "ix_calendar_workspace_type",
    CalendarEvent.workspace_id,
    CalendarEvent.event_type,
)
