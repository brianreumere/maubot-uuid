import uuid

from maubot import Plugin, MessageEvent
from maubot.handlers import command


class UuidBot(Plugin):
    @command.new()
    async def uuid(self, evt: MessageEvent) -> None:
        await evt.reply(f"`{uuid.uuid4()}`")
