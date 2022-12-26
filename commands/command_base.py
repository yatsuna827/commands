from abc import ABC
from enum import Enum
from typing import Iterable


class Variables(Enum):
    VAR_0 = 0
    VAR_1 = 1
    VAR_2 = 2


class Context:
    variables: tuple[int, int, int]

    def __init__(self) -> None:
        self.variables = [0, 0, 0]

    def out(self, value: str):
        print(value)


class Term:
    def __init__(self, value: Variables | int) -> None:
        self._value = value
        if isinstance(value, int):
            self._label = str(value)
        else:
            self._label = value.name

    @property
    def label(self) -> str:
        return self._label

    def resolve(self, context: Context) -> int:
        if isinstance(self._value, int):
            return self._value
        else:
            return context.variables[self._value.value]

    def __str__(self) -> str:
        return self.label


class Command(ABC):
    def exec(self, context: Context) -> None:
        pass


class Set(Command):
    def __init__(self, target: Variables, value: Variables | int) -> None:
        self._target = target
        self._value = Term(value)

    def exec(self, context: Context):
        context.variables[self._target.value] = self._value.resolve(context)


class Loop(Command):
    def __init__(self, times: int, commands: Iterable[Command]) -> None:
        self._times = times
        self._commands = commands

    def exec(self, context: Context) -> None:
        for _ in range(self._times):
            for command in self._commands:
                command.exec(context)


class Print(Command):
    def __init__(self, message: str) -> None:
        self._message = message

    def exec(self, context: Context) -> None:
        context.out(self._message)


class CommandStream(Command):
    def __init__(self, commands: Iterable[Command]) -> None:
        self._commands = commands

    def exec(self, context: Context = Context()):
        for command in self._commands:
            command.exec(context)
