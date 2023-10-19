# TODO: Modelar numa tabela SQL um personagem, único, baseado no ID de usuário do Discord.]
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Character(DeclarativeBase):
    __table__ = 'user_character'

    id: Mapped[str] = mapped_column( # User o ID de usuário do discord. 
        primary_key=True,
        autoincrement=False,
    )

