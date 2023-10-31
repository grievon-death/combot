from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class BaseTable(AsyncAttrs, DeclarativeBase):
    """
    Base obrigatória para declaração de tabelas.
    """
    pass
