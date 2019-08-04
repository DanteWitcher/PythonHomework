from ..enums.types import Types
from ..operators.operators import operators


class Parser:
    def __init__(self, args: str):
        self.args = args
        self.type = Types.EVAL.name

    def get_str(self) -> str:
        return self.args

    def get_type(self) -> str:
        return self.type

    def parse(self) -> None:
        for operator in operators:
            if self.args.find(operator['value']) != -1:

                self.args = self.args.replace(operator['value'], operator['right_value'])

                if operator['type'] == Types.EXEC:
                    self.type = Types.EXEC.name

                if operator['type'] == Types.ERROR:
                    self.type = Types.ERROR.name

        return None
