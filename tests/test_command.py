from commands import CommandStream, Context, Loop, Print, Set, Variables


def test_set_command():
    ctx = Context()
    command = Set(Variables.VAR_0, 10)
    assert ctx.variables == [0, 0, 0]
    command.exec(ctx)
    assert ctx.variables == [10, 0, 0]

    command = Set(Variables.VAR_1, Variables.VAR_0)
    command.exec(ctx)
    assert ctx.variables == [10, 10, 0]


def test_multiple_commands():
    ctx = Context()
    command = CommandStream(
        [
            Set(Variables.VAR_0, 10),
            Set(Variables.VAR_1, Variables.VAR_0),
            Set(Variables.VAR_2, 827),
        ]
    )

    assert ctx.variables == [0, 0, 0]

    command.exec(ctx)

    assert ctx.variables == [10, 10, 827]


class MockContext(Context):
    message: str

    def __init__(self) -> None:
        self.message = ""

    def out(self, message: str):
        self.message += message


def test_print_command():
    ctx = MockContext()
    command = Print("abc")
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "abc"


def test_loop_command():
    ctx = MockContext()
    command = Loop(3, [Print("a"), Print("b"), Print("c")])
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "abcabcabc"
