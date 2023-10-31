import logging
from core.bot.client import client

_log = logging.getLogger(__name__)


@client.event
async def on_ready() -> None:
    _log.info('Estamos online com o bot {}'.format(
        client.user,
    ))


@client.event
async def on_message(message: object) -> None:
    if message.author == client.user:
        _log.debug('Bot message.')
        return
    
    if message.content.startswith('ping'):
        await message.channel.send('pong')
