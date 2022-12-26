from .command_base import Command, Context


class Print(Command):
    def __init__(self, message: str) -> None:
        self._message = message

    def exec(self, context: Context) -> None:
        context.out(self._message)
