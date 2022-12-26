from commands import Context, Set, Variables


def test_set_command():
    ctx = Context()
    command = Set(Variables.VAR_0, 10)
    assert ctx.variables == [0, 0, 0]
    command.exec(ctx)
    assert ctx.variables == [10, 0, 0]

    command = Set(Variables.VAR_1, Variables.VAR_0)
    command.exec(ctx)
    assert ctx.variables == [10, 10, 0]
