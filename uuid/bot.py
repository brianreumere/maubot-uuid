import uuid

from maubot import Plugin, MessageEvent
from maubot.handlers import command


class Uuid(Plugin):
    @command.new()
    async def uuid(self, evt: MessageEvent) -> None:
        await evt.reply(str(uuid.uuid4()))
