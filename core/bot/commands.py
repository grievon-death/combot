import logging

from discord import Embed

from core.utils.custom_erros import BotError
from core.models.sql.chars import Character, PossibleClasses
from core.bot.Client import client

_log = logging.getLogger(__name__)


@client.command(aliases=['start', 'inciar', 'create'])
async def init(bot: object, *args: str) -> str:
    """
    Inicia o seu personagem no jogo.
    Argumento obrigatório:
        job=Classe escolhida.

    Em caso de dúvidas, veja o --help.
    """
    _log.debug('Debugando o comando init.')
    if not args:
        _log.debug(BotError.argsNotFound)
        return await bot.send(BotError.argsNotFound)

    return await bot.send('Comando funcinoando, agora só falta terminar.')
