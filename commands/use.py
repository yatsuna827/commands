from typing import Callable

from .command_base import Command, Context, Variables


class Use(Command):
    def __init__(self, target: Variables, callback: Callable[[int], None]) -> None:
        self._target = target
        self._callback = callback

    def exec(self, context: Context):
        self._callback(context.variables[self._target.value])
