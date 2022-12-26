from commands import CommandStream, Context, Set, Variables


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
