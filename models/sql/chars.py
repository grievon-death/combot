# TODO: Modelar numa tabela SQL um personagem, único, baseado no ID de usuário do Discord.]
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from models.sql.classes import PossibleClasses


class Character(DeclarativeBase):
    __table__ = 'user_character'

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
        defaul=100,
    )
    atack: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    defense: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )
    job: Mapped[PossibleClasses] = relationship(
        back_populates='user_character',
        nullable=True,
    )
    # TODO: Varificar uma forma de fazer a bolsa.
    # Talvez salvar no Mongo e recuperar de lá.
