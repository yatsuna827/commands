from inspect import signature
from typing import Callable, Iterable

from .command_base import Command, Context, ReturnCode


class If(Command):
    def __init__(
        self, predicate: Callable[[], bool] | Callable[[Context], bool], commands: Command | Iterable[Command]
    ) -> None:
        self._predicate: Callable[[Context], bool] = (
            predicate if len(signature(predicate).parameters) == 1 else lambda ctx: predicate()  # type: ignore
        )
        self._commands = [commands] if isinstance(commands, Command) else commands

    def exec(self, context: Context) -> ReturnCode | None:
        if self._predicate(context):
            for command in self._commands:
                code = command.exec(context)
                match code:
                    case ReturnCode.BREAK:
                        return ReturnCode.BREAK
                    case ReturnCode.CONTINUE:
                        return ReturnCode.CONTINUE
                    case ReturnCode.EXIT:
                        return ReturnCode.EXIT

        return ReturnCode.DEFAULT
