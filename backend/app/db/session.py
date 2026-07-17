from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,

    pool_pre_ping=True,
    pool_size=20,
    max_overflow=40,
    pool_timeout=30,
    pool_recycle=1800,

    pool_reset_on_return="rollback",
)


SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


class DatabaseSession:

    def __init__(self) -> None:
        self.session: AsyncSession | None = None

    async def __aenter__(self) -> AsyncSession:
        self.session = SessionLocal()
        return self.session

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:

        if self.session is None:
            return

        try:

            if exc:
                await self.session.rollback()
            else:
                await self.session.commit()

        finally:
            await self.session.close()


@asynccontextmanager
async def session_scope() -> AsyncGenerator[AsyncSession, None]:

    async with DatabaseSession() as session:
        yield session


async def get_db() -> AsyncGenerator[AsyncSession, None]:

    async with session_scope() as session:
        yield session


async def healthcheck() -> bool:
    """
    Проверка подключения к PostgreSQL.
    """

    try:

        async with engine.begin() as conn:
            await conn.run_sync(lambda _: None)

        return True

    except SQLAlchemyError:
        return False


async def dispose_engine() -> None:
    """
    Корректное завершение пула соединений.
    """

    await engine.dispose()
