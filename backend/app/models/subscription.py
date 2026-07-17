from __future__ import annotations

import enum
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class SubscriptionStatus(str, enum.Enum):
    TRIAL = "trial"
    ACTIVE = "active"
    PAST_DUE = "past_due"
    SUSPENDED = "suspended"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class BillingPeriod(str, enum.Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"
    LIFETIME = "lifetime"


class Subscription(BaseModel):
    __tablename__ = "subscriptions"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )

    created_by_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    plan_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    plan_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[SubscriptionStatus] = mapped_column(
        Enum(SubscriptionStatus),
        default=SubscriptionStatus.TRIAL,
        nullable=False,
        index=True,
    )

    billing_period: Mapped[BillingPeriod] = mapped_column(
        Enum(BillingPeriod),
        default=BillingPeriod.MONTHLY,
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="USD",
        nullable=False,
    )

    seats: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    trial_ends_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    current_period_start: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    current_period_end: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    cancelled_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    renews_automatically: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    external_provider: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    external_subscription_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
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
    "ix_subscription_status",
    Subscription.status,
)

Index(
    "ix_subscription_period_end",
    Subscription.current_period_end,
)

Index(
    "ix_subscription_provider",
    Subscription.external_provider,
)
