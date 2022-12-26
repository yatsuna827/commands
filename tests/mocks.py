from commands import Context


class MockContext(Context):
    message: str

    def __init__(self) -> None:
        self.message = ""

    def out(self, message: str):
        self.message += message
