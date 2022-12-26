from .command_base import Command, Context, Term, Variables


class Subtract(Command):
    def __init__(self, target: Variables, value: Variables | int) -> None:
        self._target = target
        self._value = Term(value)

    def exec(self, context: Context):
        context.variables[self._target.value] -= self._value.resolve(context)
