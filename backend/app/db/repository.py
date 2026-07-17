from __future__ import annotations

from typing import Any, Generic, TypeVar

from sqlalchemy import Select, delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from app.models.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepository(Generic[ModelType]):
    """
    Универсальный Repository.

    От него наследуются все остальные репозитории проекта.
    """

    model: DeclarativeMeta

    def __init__(self, session: AsyncSession):
        self.session = session

    # --------------------------------------------------
    # Query
    # --------------------------------------------------

    def query(self) -> Select[Any]:
        return select(self.model)

    # --------------------------------------------------
    # GET
    # --------------------------------------------------

    async def get(
        self,
        object_id,
    ) -> ModelType | None:

        stmt = self.query().where(
            self.model.id == object_id,
            self.model.is_deleted.is_(False),
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_or_404(
        self,
        object_id,
    ) -> ModelType:

        obj = await self.get(object_id)

        if obj is None:
            raise ValueError(
                f"{self.model.__name__} not found"
            )

        return obj

    async def exists(
        self,
        **filters,
    ) -> bool:

        stmt = (
            select(func.count())
            .select_from(self.model)
            .filter_by(**filters)
        )

        result = await self.session.execute(stmt)

        return result.scalar_one() > 0

    # --------------------------------------------------
    # LIST
    # --------------------------------------------------

    async def list(
        self,
        *,
        offset: int = 0,
        limit: int = 50,
        order_by=None,
        **filters,
    ) -> list[ModelType]:

        stmt = (
            self.query()
            .filter_by(**filters)
            .where(self.model.is_deleted.is_(False))
            .offset(offset)
            .limit(limit)
        )

        if order_by is not None:
            stmt = stmt.order_by(order_by)

        result = await self.session.execute(stmt)

        return list(result.scalars().all())

    async def count(
        self,
        **filters,
    ) -> int:

        stmt = (
            select(func.count())
            .select_from(self.model)
            .filter_by(**filters)
            .where(self.model.is_deleted.is_(False))
        )

        result = await self.session.execute(stmt)

        return result.scalar_one()

    # --------------------------------------------------
    # CREATE
    # --------------------------------------------------

    async def create(
        self,
        **data,
    ) -> ModelType:

        obj = self.model(**data)

        self.session.add(obj)

        await self.session.flush()

        await self.session.refresh(obj)

        return obj

    # --------------------------------------------------
    # UPDATE
    # --------------------------------------------------

    async def update(
        self,
        obj: ModelType,
        **data,
    ) -> ModelType:

        for key, value in data.items():
            setattr(obj, key, value)

        await self.session.flush()

        await self.session.refresh(obj)

        return obj

    # --------------------------------------------------
    # SOFT DELETE
    # --------------------------------------------------

    async def soft_delete(
        self,
        obj: ModelType,
    ) -> None:

        obj.soft_delete()

        await self.session.flush()

    # --------------------------------------------------
    # RESTORE
    # --------------------------------------------------

    async def restore(
        self,
        obj: ModelType,
    ) -> None:

        obj.is_deleted = False
        obj.deleted_at = None

        await self.session.flush()

    # --------------------------------------------------
    # HARD DELETE
    # --------------------------------------------------

    async def delete(
        self,
        obj: ModelType,
    ) -> None:

        await self.session.delete(obj)

    async def delete_by_id(
        self,
        object_id,
    ) -> None:

        stmt = delete(self.model).where(
            self.model.id == object_id
        )

        await self.session.execute(stmt)

    # --------------------------------------------------
    # SAVE
    # --------------------------------------------------

    async def save(
        self,
    ) -> None:

        await self.session.commit()
