from .command_base import Command, Context, ReturnCode


class Exit(Command):
    def exec(self, context: Context):
        return ReturnCode.EXIT
