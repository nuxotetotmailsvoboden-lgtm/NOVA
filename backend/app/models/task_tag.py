from __future__ import annotations

import uuid

from sqlalchemy import (
    ForeignKey,
    Index,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class TaskTag(BaseModel):
    """
    Связующая таблица между задачами и тегами.
    """

    __tablename__ = "task_tags"

    __table_args__ = (
        UniqueConstraint(
            "task_id",
            "tag_id",
            name="uq_task_tag",
        ),
    )

    task_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    tag_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tags.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )


Index(
    "ix_task_tags_task",
    TaskTag.task_id,
)

Index(
    "ix_task_tags_tag",
    TaskTag.tag_id,
)
