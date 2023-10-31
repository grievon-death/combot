from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models.sql.base import BaseTable


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


def migration(engine: object) -> None:
    PossibleClasses.metadata.create_all(engine)
