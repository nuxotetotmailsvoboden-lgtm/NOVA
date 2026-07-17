from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class UserRole(str, enum.Enum):
    SUPER_ADMIN = "super_admin"
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"


class UserStatus(str, enum.Enum):
    PENDING = "pending"
    ACTIVE = "active"
    BLOCKED = "blocked"
    DELETED = "deleted"


class User(BaseModel):
    __tablename__ = "users"

    # -----------------------
    # Basic
    # -----------------------

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    username: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
        index=True,
    )

    full_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    avatar: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # -----------------------
    # Telegram
    # -----------------------

    telegram_id: Mapped[int | None] = mapped_column(
        nullable=True,
        unique=True,
        index=True,
    )

    telegram_username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    telegram_first_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    telegram_last_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    telegram_photo_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # -----------------------
    # Security
    # -----------------------

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.USER,
        nullable=False,
        index=True,
    )

    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus),
        default=UserStatus.PENDING,
        nullable=False,
        index=True,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    two_factor_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # -----------------------
    # Login
    # -----------------------

    login_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    failed_login_attempts: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # -----------------------
    # Audit
    # -----------------------

    created_by_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    updated_by_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    # -----------------------
    # Relations
    # -----------------------

    created_by: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[created_by_id],
        remote_side="User.id",
        lazy="joined",
    )

    updated_by: Mapped["User | None"] = relationship(
        "User",
        foreign_keys=[updated_by_id],
        remote_side="User.id",
        lazy="joined",
    )
