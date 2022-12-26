from commands import Variables, Set, CommandStream, Context, Loop


def test_set_command():
  ctx = Context()
  command = Set(Variables.VAR_0, 10)
  assert ctx.variables == [0,0,0]
  command.exec(ctx)
  assert ctx.variables == [10, 0, 0]

  command = Set(Variables.VAR_1, Variables.VAR_0)
  command.exec(ctx)
  assert ctx.variables == [10, 10, 0]


def test_multiple_commands():
  ctx = Context()
  command = CommandStream([
    Set(Variables.VAR_0, 10),
    Set(Variables.VAR_1, Variables.VAR_0),
    Set(Variables.VAR_2, 827)
  ])

  assert ctx.variables == [0,0,0]

  command.exec(ctx)

  assert ctx.variables == [10, 10, 827]


def test_loop_command():
  ctx = Context()
  
  command = Loop(3, [
    Set(Variables.VAR_0, 10),
    Set(Variables.VAR_1, Variables.VAR_0),
    Set(Variables.VAR_2, 827)
  ])
