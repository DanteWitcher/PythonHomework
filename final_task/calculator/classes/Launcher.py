from .Parser import Parser


class Launcher:
    def __init__(self, input_string: str):
        self.input = input_string

    def run(self) -> None:
        Parser(self.input).parse()

        return None
