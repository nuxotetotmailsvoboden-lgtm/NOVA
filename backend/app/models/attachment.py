from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    BigInteger,
    Enum,
    ForeignKey,
    Index,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class AttachmentType(str, enum.Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    PDF = "pdf"
    ARCHIVE = "archive"
    OTHER = "other"


class Attachment(BaseModel):
    __tablename__ = "attachments"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    uploaded_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
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

    task_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    note_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("notes.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    original_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    extension: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    storage_path: Mapped[str] = mapped_column(
        String(1024),
        nullable=False,
        unique=True,
    )

    attachment_type: Mapped[AttachmentType] = mapped_column(
        Enum(AttachmentType),
        nullable=False,
        index=True,
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )

    uploaded_by: Mapped["User | None"] = relationship(
        "User",
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

    task: Mapped["Task | None"] = relationship(
        "Task",
        lazy="joined",
    )

    note: Mapped["Note | None"] = relationship(
        "Note",
        lazy="joined",
    )


Index(
    "ix_attachment_workspace",
    Attachment.workspace_id,
)

Index(
    "ix_attachment_client",
    Attachment.client_id,
)

Index(
    "ix_attachment_deal",
    Attachment.deal_id,
)

Index(
    "ix_attachment_task",
    Attachment.task_id,
)

Index(
    "ix_attachment_note",
    Attachment.note_id,
)

Index(
    "ix_attachment_type",
    Attachment.attachment_type,
)
