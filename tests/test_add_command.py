from commands import Add, Context, Variables


def test_set_command():
    ctx = Context()
    add_10_to_var0 = Add(Variables.VAR_0, 10)
    add_var0_to_var1 = Add(Variables.VAR_1, Variables.VAR_0)
    assert ctx.variables == [0, 0, 0]

    add_10_to_var0.exec(ctx)
    assert ctx.variables == [10, 0, 0]

    add_var0_to_var1.exec(ctx)
    assert ctx.variables == [10, 10, 0]

    add_10_to_var0.exec(ctx)
    assert ctx.variables == [20, 10, 0]

    add_10_to_var0.exec(ctx)
    assert ctx.variables == [30, 10, 0]

    add_var0_to_var1.exec(ctx)
    assert ctx.variables == [30, 40, 0]
