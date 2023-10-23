
from sqlalchemy.orm import Mapped, mapped_column

from models.cursors import SqlBase


class PossibleClasses(SqlBase):
    __table__ = 'possible_classes'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )
    life: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    energy: Mapped[int] = mapped_column(
        nullable=False,
        defaul=5,
    )
    atack: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    defense: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
