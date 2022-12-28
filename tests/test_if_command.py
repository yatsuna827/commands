from commands import Add, Break, Continue, If, Loop, Print, Variables
from tests.mocks import MockContext


def test_if_command():
    ctx = MockContext()

    If(lambda: False, [Print("a"), Print("b"), Print("c")]).exec(ctx)
    assert ctx.message == ""

    If(lambda: True, [Print("a"), Print("b"), Print("c")]).exec(ctx)
    assert ctx.message == "abc"


def test_if_command_use_ctx():
    ctx = MockContext()

    # fmt: off
    Loop(10, [
        Add(Variables.VAR_0, 1),
        Print("a"),
        If(lambda ctx: ctx.variables[0] == 5, Break()),
    ]).exec(ctx)
    # fmt: on

    assert ctx.variables == [5, 0, 0]
    assert ctx.message == "aaaaa"


def test_if_break_1():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Print("a"),
        Print("b"),
        If(lambda: True, Break()),
        Print("c"),
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "ab"


def test_if_break_2():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Print("a"),
        Print("b"),
        If(lambda: False, Break()),
        Print("c"),
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "abcabcabc"


def test_if_break_3():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Print("a"),
        Print("b"),
        If(lambda: True, [
            Print("!"),
            Break()
        ]),
        Print("c"),
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "ab!"


def test_if_continue():
    ctx = MockContext()
    # fmt: off
    command = Loop(3, [
        Print("a"),
        Print("b"),
        If(lambda: True, Continue()),
        Print("c"),
    ])
    # fmt: on
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "ababab"
