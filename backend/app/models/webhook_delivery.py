from __future__ import annotations

import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    JSON,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class WebhookDeliveryStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"
    RETRYING = "retrying"
    CANCELLED = "cancelled"


class WebhookDelivery(BaseModel):
    __tablename__ = "webhook_deliveries"

    webhook_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("webhooks.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    status: Mapped[WebhookDeliveryStatus] = mapped_column(
        Enum(WebhookDeliveryStatus),
        default=WebhookDeliveryStatus.PENDING,
        nullable=False,
        index=True,
    )

    request_method: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    request_url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False,
    )

    request_headers: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    request_body: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    response_status_code: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    response_headers: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    response_body: Mapped[dict | str | None] = mapped_column(
        JSON,
        nullable=True,
    )

    attempts: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    max_attempts: Mapped[int] = mapped_column(
        Integer,
        default=3,
        nullable=False,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    duration_ms: Mapped[float | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    webhook: Mapped["Webhook"] = relationship(
        "Webhook",
        lazy="joined",
    )

    workspace: Mapped["Workspace"] = relationship(
        "Workspace",
        lazy="joined",
    )


Index(
    "ix_webhook_delivery_workspace",
    WebhookDelivery.workspace_id,
)

Index(
    "ix_webhook_delivery_status",
    WebhookDelivery.status,
)

Index(
    "ix_webhook_delivery_webhook",
    WebhookDelivery.webhook_id,
)

Index(
    "ix_webhook_delivery_started",
    WebhookDelivery.started_at,
)
