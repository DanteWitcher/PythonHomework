from math import *

from ..enums.types import Types


class Launcher:
    def __init__(self, input_string: str):
        self.input = input_string

    def __exec(self) -> None:
        exec('print({:s})'.format(self.input),
             {'sin': sin, 'print': print, 'log': log, 'log10': log10, 'pi': pi, 'e': e, 'pow': pow, 'abs': abs,
              'cos': cos})
        return None

    def __eval(self) -> None:
        print(eval(self.input))

        return None

    def __error(self) -> None:
        print('ERROR: `{:s}` is not correct operator'.format(self.input))

        return None

    def run(self, run_type: Types) -> None:
        if run_type == Types.EXEC.name:
            self.__exec()

        if run_type == Types.EVAL.name:
            self.__eval()

        if run_type == Types.ERROR.name:
            self.__error()

        return None
