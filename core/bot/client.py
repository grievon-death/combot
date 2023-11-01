import logging

import discord


class Client(discord.Client):
    _log = logging.getLogger(__name__)

    async def on_ready(self) -> None:
        self._log.info('Logado com %s' % self.user)

    async def on_message(self, message) -> None:
        if message.author == self.user:
            # Ignora a mensagem do próprio BOT.
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            self._log.debug('Pong response')
