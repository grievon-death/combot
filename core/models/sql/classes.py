from typing import NewType, Dict

from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, selectinload
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from core.models.sql.base import BaseTable

QueryType = NewType('PossibleClass', object)

class PossibleClasses(BaseTable):
    __tablename__ = 'possible_classes'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
    )
    life: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    energy: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    atack: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    defense: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    speed: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )

    @staticmethod
    async def query(session: async_sessionmaker[AsyncSession], **kwargs: Dict) -> tuple[QueryType]:
        async with session() as conn:
            _stmt = select(PossibleClasses).options(selectinload(PossibleClasses.name))
            _result = await session.execute(_stmt)
        
            return _result.scalars()

    @staticmethod
    async def insert(session: async_sessionmaker[AsyncSession], **kwargs: Dict) -> None:
        return


async def migration(engine: object) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(PossibleClasses.metadata.create_all)
    