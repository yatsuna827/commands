from commands import Print
from tests.mocks import MockContext


def test_print_command():
    ctx = MockContext()
    command = Print("abc")
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "abc"
