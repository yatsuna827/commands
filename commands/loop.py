from typing import Iterable

from .command_base import Command, Context


class Loop(Command):
    def __init__(self, times: int, commands: Iterable[Command]) -> None:
        self._times = times
        self._commands = commands

    def exec(self, context: Context) -> None:
        for _ in range(self._times):
            for command in self._commands:
                command.exec(context)