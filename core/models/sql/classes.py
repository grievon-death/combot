from typing import NewType, Dict, List

from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, selectinload
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from core.models.sql.base import BaseTable
from core.models.cursors import sql_engine

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
    async def query(statement: select) -> tuple[QueryType]:
        session = async_sessionmaker(sql_engine)
        async with session() as _session:
            # _stmt = select(PossibleClasses).options(selectinload(PossibleClasses.name))
            _result = await _session.execute(statement)

        return _result.scalars().one()

    @staticmethod
    async def insert(
        name: str,
        life: int,
        energy: int,
        atack: int,
        defense: int,
        speed: int
    ) -> None:
        session = async_sessionmaker(sql_engine)

        async with session() as _session:
            _session.add(PossibleClasses(
                name=name,
                life=life,
                energy=energy,
                atack=atack,
                defense=defense,
                speed=speed,
            ))
            await _session.commit()

        await sql_engine.dispose()


async def migration(engine: object) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(PossibleClasses.metadata.create_all)
