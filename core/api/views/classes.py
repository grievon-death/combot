import asyncio

from tornado.web import RequestHandler
from sqlalchemy.ext.asyncio import async_sessionmaker

from core.models.sql.classes import PossibleClasses
from core.models.cursors import sql_engine


class PossibleClassesView(RequestHandler):
    _session = async_sessionmaker(sql_engine, expire_on_commit=False)

    async def get(self) -> dict:
        _classes = await PossibleClasses.query(self._session)

        self.finish({
            'data': [_class.__dict__ for _class in _classes] 
        })

        await sql_engine.dispose()  # Fecha as conexões depois de concluir a consulta.
