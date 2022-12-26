from abc import ABC
from typing import Generator, Sequence
from enum import Enum

class Variables(Enum):
  VAR_0 = 0
  VAR_1 = 1
  VAR_2 = 2



class Context:
  variables: tuple[int, int, int]

  def __init__(self) -> None:
    self.variables = [0,0,0]


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


class CommandStream(Command):
  def __init__(self, commands: Sequence[Command]) -> None:
    self._commands = commands

  def exec(self, context: Context = Context()) -> Generator[str, None, None]:
    for command in self._commands:
      command.exec(context)
