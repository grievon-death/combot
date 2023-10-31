from discord import Client, Intents

_intents: Intents = Intents.default()
_intents.message_content=True

client: Client = Client(intents=_intents)
