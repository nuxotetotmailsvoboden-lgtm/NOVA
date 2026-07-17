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


class DealTag(BaseModel):
    """
    Связующая таблица между сделками и тегами.
    """

    __tablename__ = "deal_tags"

    __table_args__ = (
        UniqueConstraint(
            "deal_id",
            "tag_id",
            name="uq_deal_tag",
        ),
    )

    deal_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("deals.id", ondelete="CASCADE"),
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
    "ix_deal_tags_deal",
    DealTag.deal_id,
)

Index(
    "ix_deal_tags_tag",
    DealTag.tag_id,
)
