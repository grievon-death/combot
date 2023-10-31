import logging

from core.models.cursors import sql_engine
from core.models.sql import classes, chars


class Command:
    """
    Comandos padrões do sistema.
    Não relacionados ao BOT | API | ETC.
    """
    _log = logging.getLogger(__name__)

    @staticmethod
    def migrate() -> None:
        """
        Realiza a migração do banco de dados.
        """
        try:
            Command._log.info('Iniciando a migração.')
            classes.migration(sql_engine)
            chars.migration(sql_engine)
        except Exception as e:
            Command._log.debug('Ops... Problemas com a migração dos dados.')
            raise Exception(e.args)

        Command._log.info('Migração finalizada.')

    @staticmethod
    def run_combot() -> None:
        """
        Comando para iniciar o BOT.
        """
        return
