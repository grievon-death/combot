from typing import Dict, List

from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import async_sessionmaker

from core.models.cursors import sql_engine
from core.models.sql.base import BaseTable
from core.models.sql.classes import PossibleClasses


class Character(BaseTable):
    __tablename__ = 'user_character'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    user: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
    )
    level: Mapped[int] = mapped_column(
        nullable=False,
        default=1,
    )
    life: Mapped[int] = mapped_column(
        nullable=False,
        default=100,
    )
    energy: Mapped[int] = mapped_column(
        nullable=False,
        default=100,
    )
    atack: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    defense: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )

    @staticmethod
    async def insert(user: str, job: str=None) -> Dict:
        """
        Criar um personagem no banco de dados para tornar o usuário jogável.
        """
        session = async_sessionmaker(sql_engine, expire_on_commit=False)

        async with session() as _session:
            async with _session.begin():
                _session.add(Character(user=user))

            stmt = select(Character)\
                .options(Character.user==user)
            _result = await _session.execute(stmt)

        await sql_engine.dispose()  # Fecha e limpa as conexões com o banco.

        return _result.scalar()


async def migration(engine: object) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Character.metadata.create_all)
