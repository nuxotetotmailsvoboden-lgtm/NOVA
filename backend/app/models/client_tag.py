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


class ClientTag(BaseModel):
    """
    Связующая таблица между клиентами и тегами.
    Один клиент может иметь несколько тегов,
    один тег может использоваться у множества клиентов.
    """

    __tablename__ = "client_tags"

    __table_args__ = (
        UniqueConstraint(
            "client_id",
            "tag_id",
            name="uq_client_tag",
        ),
    )

    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients.id", ondelete="CASCADE"),
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
    "ix_client_tags_client",
    ClientTag.client_id,
)

Index(
    "ix_client_tags_tag",
    ClientTag.tag_id,
)
