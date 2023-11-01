import logging

from discord import Embed, Intents
from discord.ext import commands

from core.bot.client import Client

_bot = commands.Bot(command_prefix='--', intents=Intents.all())


class Bot(Client):
    _log = logging.getLogger(__name__)

    @_bot.command(aliases=['start', 'strt', 'inciar'])
    async def init(bot: object, *args: str) -> str:
        """
        Inicia o seu personagem no jogo.
        """
        return await bot.send('Comando funcinoando, agora só falta terminar.')
