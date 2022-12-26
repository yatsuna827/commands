from commands import Context, Set, Use, Variables


def test_use_command():
    ctx = Context()
    global a
    a = 0
    def f(x: int):
        global a
        a = x

    command = Use(Variables.VAR_0, f)
    assert a == 0
    
    Set(Variables.VAR_0, 777).exec(ctx)
    command.exec(ctx)
    assert a == 777
