from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Iterable


class Variables(Enum):
    VAR_0 = 0
    VAR_1 = 1
    VAR_2 = 2


class Context:
    variables: list[int]

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


class ReturnCode(Enum):
    DEFAULT = auto()
    BREAK = auto()
    CONTINUE = auto()
    EXIT = auto()


class Command(ABC):
    @abstractmethod
    def exec(self, context: Context) -> ReturnCode | None:
        pass


class CommandStream(Command):
    def __init__(self, commands: Iterable[Command]) -> None:
        self._commands = commands

    def exec(self, context: Context = Context()):
        for command in self._commands:
            code = command.exec(context)
            if code == ReturnCode.EXIT:
                return code

        return ReturnCode.DEFAULT
