from __future__ import annotations

import enum
import uuid

from sqlalchemy import (
    Boolean,
    Enum,
    ForeignKey,
    Index,
    JSON,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class WebhookDirection(str, enum.Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"


class WebhookStatus(str, enum.Enum):
    ACTIVE = "active"
    DISABLED = "disabled"


class WebhookMethod(str, enum.Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class WebhookAuthType(str, enum.Enum):
    NONE = "none"
    BEARER = "bearer"
    BASIC = "basic"
    API_KEY = "api_key"
    HMAC = "hmac"


class Webhook(BaseModel):
    __tablename__ = "webhooks"

    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    created_by_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    direction: Mapped[WebhookDirection] = mapped_column(
        Enum(WebhookDirection),
        nullable=False,
        index=True,
    )

    method: Mapped[WebhookMethod] = mapped_column(
        Enum(WebhookMethod),
        default=WebhookMethod.POST,
        nullable=False,
    )

    status: Mapped[WebhookStatus] = mapped_column(
        Enum(WebhookStatus),
        default=WebhookStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    auth_type: Mapped[WebhookAuthType] = mapped_column(
        Enum(WebhookAuthType),
        default=WebhookAuthType.NONE,
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(2048),
        nullable=False,
    )

    headers: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    auth_config: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )

    events: Mapped[list] = mapped_column(
        JSON,
        default=list,
        nullable=False,
    )

    retry_count: Mapped[int] = mapped_column(
        default=3,
        nullable=False,
    )

    timeout_seconds: Mapped[int] = mapped_column(
        default=30,
        nullable=False,
    )

    verify_ssl: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_system: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
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
    "ix_webhook_workspace_status",
    Webhook.workspace_id,
    Webhook.status,
)

Index(
    "ix_webhook_workspace_direction",
    Webhook.workspace_id,
    Webhook.direction,
)

Index(
    "ix_webhook_workspace_method",
    Webhook.workspace_id,
    Webhook.method,
)
