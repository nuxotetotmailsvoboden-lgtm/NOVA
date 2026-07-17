from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Enum,
    ForeignKey,
    Index,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class NoteType(str, enum.Enum):
    NOTE = "note"
    CALL = "call"
    EMAIL = "email"
    MEETING = "meeting"
    TELEGRAM = "telegram"
    WHATSAPP = "whatsapp"
    SYSTEM = "system"


class Note(BaseModel):
    __tablename__ = "notes"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    client_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    deal_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("deals.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    author_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    note_type: Mapped[NoteType] = mapped_column(
        Enum(NoteType),
        default=NoteType.NOTE,
        nullable=False,
        index=True,
    )

    title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    client: Mapped["Client | None"] = relationship(
        "Client",
        lazy="joined",
    )

    deal: Mapped["Deal | None"] = relationship(
        "Deal",
        lazy="joined",
    )

    author: Mapped["User"] = relationship(
        "User",
        lazy="joined",
    )


Index(
    "ix_note_workspace_client",
    Note.workspace_id,
    Note.client_id,
)

Index(
    "ix_note_workspace_deal",
    Note.workspace_id,
    Note.deal_id,
)

Index(
    "ix_note_workspace_type",
    Note.workspace_id,
    Note.note_type,
)
