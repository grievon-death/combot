import asyncio
import logging

from discord import Intents

from core.api.app import app
from core.bot.commands import Bot
from core.models.cursors import sql_engine
from core.models.sql import classes, chars
from settings.general import BOT_TOKEN


class Command:
    """
    Comandos padrões do sistema.
    Não relacionados ao BOT | API | ETC.
    """
    _log = logging.getLogger(__name__)

    @staticmethod
    async def migrate() -> None:
        """
        Realiza a migração do banco de dados.
        """
        try:
            Command._log.info('Iniciando a migração.')
            await classes.migration(sql_engine)
            await chars.migration(sql_engine)
        except Exception as e:
            Command._log.debug('Ops... Problemas com a migração dos dados.')
            raise Exception(e.args)

        Command._log.info('Migração finalizada.')

    @staticmethod
    def run_combot() -> None:
        """
        Comando para iniciar o BOT.
        """
        _intents: Intents = Intents.default()
        _intents.message_content=True
        _client = Bot(intents=_intents)
        _client.run(BOT_TOKEN)

    @staticmethod
    async def run_api() -> None:
        _app = app()
        _app.listen(5000)    
        shutdown_event = asyncio.Event()
        await shutdown_event.wait()
