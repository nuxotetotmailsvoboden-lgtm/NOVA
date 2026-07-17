from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Index,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class RefreshToken(BaseModel):
    __tablename__ = "refresh_tokens"

    # Пользователь
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # JTI (уникальный идентификатор JWT)
    jti: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
        index=True,
    )

    # Храним только хэш refresh token
    token_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    # Истечение срока действия
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    # Когда был использован
    used_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Когда был отозван
    revoked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Причина отзыва
    revoke_reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Клиентские данные
    ip_address: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    user_agent: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    device_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        lazy="joined",
    )

    @property
    def is_expired(self) -> bool:
        return datetime.utcnow() >= self.expires_at.replace(tzinfo=None)

    @property
    def is_revoked(self) -> bool:
        return self.revoked_at is not None

    @property
    def is_used(self) -> bool:
        return self.used_at is not None

    @property
    def can_be_used(self) -> bool:
        return (
            self.is_active
            and not self.is_expired
            and not self.is_revoked
            and not self.is_used
        )


Index(
    "ix_refresh_tokens_user_active",
    RefreshToken.user_id,
    RefreshToken.is_active,
)

Index(
    "ix_refresh_tokens_expires",
    RefreshToken.expires_at,
)
