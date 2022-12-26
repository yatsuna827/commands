from commands import Variables, Set, CommandStream, Context


def test_set_command():
  ctx = Context()
  Set(Variables.VAR_0, 10).exec(ctx)
  assert ctx.variables == [10, 0, 0]

  Set(Variables.VAR_1, Variables.VAR_0).exec(ctx)
  assert ctx.variables == [10, 10, 0]


def test_multiple_commands():
  ctx = Context()
  CommandStream([
    Set(Variables.VAR_0, 10),
    Set(Variables.VAR_1, Variables.VAR_0),
    Set(Variables.VAR_2, 827)
  ]).exec(ctx)

  assert ctx.variables == [10, 10, 827]
