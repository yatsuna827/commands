from commands import Break, Loop, Print
from tests.mocks import MockContext


def test_loop_command():
    ctx = MockContext()
    command = Loop(3, [Print("a"), Print("b"), Print("c")])
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "abcabcabc"

def test_break_loop():
    ctx = MockContext()
    command = Loop(3, [
        Print("a"),
        Print("b"),
        Break(), 
        Print("c"),
    ])
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "ab"

def test_nested_loop():
    ctx = MockContext()
    command = Loop(3, [
        Loop(3, [
            Print("a"),
        ]),
        Print("!")
    ])
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "aaa!aaa!aaa!"

def test_nested_loop():
    ctx = MockContext()
    command = Loop(3, [
        Loop(3, [
            Print("a"),
            Break(),
            Print("b")
        ]),
        Print("!")
    ])
    assert ctx.message == ""

    command.exec(ctx)
    assert ctx.message == "a!a!a!"
