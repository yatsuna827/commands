from commands import Break, Continue, Loop, Print
from tests.mocks import MockContext


def test_loop_command():
    ctx = MockContext()
    command = Loop(3, [Print("a"), Print("b"), Print("c")])
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "abcabcabc"


def test_break_loop():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Print("a"),
        Print("b"),
        Break(),
        Print("c"),
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "ab"


def test_continue_loop():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Print("a"),
        Print("b"),
        Continue(),
        Print("c"),
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "ababab"


def test_nested_loop():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Loop(3, [
            Print("a"),
        ],),
        Print("!"),
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "aaa!aaa!aaa!"


def test_nested_break():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Loop(3, [
            Print("a"),
            Break(),
            Print("b")
        ]),
        Print("!")
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "a!a!a!"


def test_nested_continue():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Loop(3, [
            Print("a"),
            Continue(),
            Print("b")
        ]),
        Print("!")
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "aaa!aaa!aaa!"
