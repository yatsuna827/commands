from itertools import repeat
from typing import Iterable

from .command_base import Command, Context, ReturnCode


class Break(Command):
    def exec(self, context: Context):
        return ReturnCode.BREAK


class Continue(Command):
    def exec(self, context: Context):
        return ReturnCode.CONTINUE


class Loop(Command):
    def __init__(self, times: int, commands: Iterable[Command]) -> None:
        self._times = times
        self._commands = commands

    def exec(self, context: Context) -> ReturnCode | None:
        for _ in repeat(0) if self._times < 0 else range(self._times):
            for command in self._commands:
                code = command.exec(context)
                match code:
                    case ReturnCode.BREAK:
                        return ReturnCode.DEFAULT
                    case ReturnCode.CONTINUE:
                        break
                    case ReturnCode.EXIT:
                        return ReturnCode.EXIT

        return ReturnCode.DEFAULT
