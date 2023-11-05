import asyncio
import logging

from core.api.app import app
from core.bot.Client import client
from core.models.cursors import sql_engine
from core.models.sql import classes, chars
from core.utils.base import get_populate_content, validate_max_points_distribituion
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
    async def populate() -> None:
        """
        Popula as classes com os tipos básicos.
        TODO: No futuro adicionar a possíbilidade de icluir apartir de uma API.
        """
        try:
            Command._log.info('Iniciando a população do banco de dados.')
            _content = await get_populate_content()

            if not await validate_max_points_distribituion(
                _content['rules']['base_max_points'],
                _content['classes']
            ):
                Command._log.error('Ops... A quantidade de pontos distribuídos não está de acordo com a pontuação máxima.')
                return
        except KeyError as e:
            Command._log.error('Ops... Chave obrigatória não encontrada {}'.format(
                e.args
            ))
            return
        except Exception as e:
            Command._log.debug('Ops... Não foi possível popular o banco de dados.\n{}'.format(
                e.args
            ))
            return

    @staticmethod
    def run_combot() -> None:
        """
        Comando para iniciar o BOT.
        """
        client.run(BOT_TOKEN)

    @staticmethod
    async def run_api() -> None:
        _app = app()
        _app.listen(5000)    
        shutdown_event = asyncio.Event()
        await shutdown_event.wait()
