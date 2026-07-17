from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import UUID

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
   deprecated="auto",
)


class SecurityError(Exception):
    pass


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def hash_password(
    password: str,
) -> str:
    return pwd_context.hash(password)


def _create_token(
    *,
    subject: str,
    expires_delta: timedelta,
    token_type: str,
    extra: dict[str, Any] | None = None,
) -> str:
    now = datetime.now(timezone.utc)

    payload: dict[str, Any] = {
        "sub": subject,
        "type": token_type,
        "iat": int(now.timestamp()),
        "nbf": int(now.timestamp()),
        "exp": int((now + expires_delta).timestamp()),
    }

    if extra:
        payload.update(extra)

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def create_access_token(
    user_id: UUID,
) -> str:
    return _create_token(
        subject=str(user_id),
        expires_delta=timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        ),
        token_type="access",
    )


def create_refresh_token(
    user_id: UUID,
) -> str:
    return _create_token(
        subject=str(user_id),
        expires_delta=timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        ),
        token_type="refresh",
    )


def decode_token(
    token: str,
) -> dict[str, Any]:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )

        return payload

    except JWTError as exc:
        raise SecurityError("Invalid token") from exc


def get_token_subject(
    token: str,
) -> UUID:
    payload = decode_token(token)

    subject = payload.get("sub")

    if not subject:
        raise SecurityError("Missing subject")

    return UUID(subject)


def ensure_token_type(
    token: str,
    token_type: str,
) -> dict[str, Any]:
    payload = decode_token(token)

    if payload.get("type") != token_type:
        raise SecurityError("Invalid token type")

    return payload
