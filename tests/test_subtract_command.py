from commands import Context, Subtract, Variables


def test_sub_command():
    ctx = Context()
    sub_10_from_var0 = Subtract(Variables.VAR_0, 10)
    sub_var0_from_var1 = Subtract(Variables.VAR_1, Variables.VAR_0)
    assert ctx.variables == [0, 0, 0]

    sub_10_from_var0.exec(ctx)
    assert ctx.variables == [-10, 0, 0]

    sub_var0_from_var1.exec(ctx)
    assert ctx.variables == [-10, 10, 0]
