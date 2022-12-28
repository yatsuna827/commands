from commands import CommandStream, Exit, If, Loop, Print, ReturnCode
from tests.mocks import MockContext


def test_if():
    ctx = MockContext()

    # fmt: off
    code = If(lambda: True, [
        Print("a"),
        Exit(),
        Print("b"),
        Print("c")
    ]).exec(ctx)
    # fmt: on
    assert ctx.message == "a"
    assert code == ReturnCode.EXIT


def test_loop():
    ctx = MockContext()
    # fmt: off
    code = Loop(3, [
        Print("a"),
        Print("b"),
        Exit(),
        Print("c"),
    ]).exec(ctx)
    # fmt: on
    assert ctx.message == "ab"
    assert code == ReturnCode.EXIT


def test_nested_loop():
    ctx = MockContext()
    # fmt: off
    code = Loop(3, [
        Loop(3, [
            Print("a"),
            Exit(),
        ]),
        Print("!"),
    ]).exec(ctx)
    # fmt: on
    assert ctx.message == "a"
    assert code == ReturnCode.EXIT


def test_stream():
    ctx = MockContext()
    # fmt: off
    code = CommandStream([
        Print("a"),
        Exit(),
        Print("a"),
    ]).exec(ctx)
    # fmt: on
    assert ctx.message == "a"
    assert code == ReturnCode.EXIT
