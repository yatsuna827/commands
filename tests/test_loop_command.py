from commands import Loop, Print
from tests.mocks import MockContext


def test_loop_command():
    ctx = MockContext()
    command = Loop(3, [Print("a"), Print("b"), Print("c")])
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "abcabcabc"
