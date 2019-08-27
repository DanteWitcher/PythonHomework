from .Stack import Stack
from types import FunctionType


class Executer:
    def __init__(self, stack_numbers: Stack, stack_operators: Stack):
        self.s_n = stack_numbers
        self.s_o = stack_operators

    def run_one_command(self):
        v_last = self.s_n.pop()

        if isinstance(v_last, FunctionType):
            last = float(v_last())
        else:
            last = float(v_last)

        result = self.s_o.pop()['operation'](last)
        self.s_n.push(str(result))

    def run_command(self):
        v_last = self.s_n.pop()
        v_last_last = self.s_n.pop()

        if isinstance(v_last, FunctionType):
            last = float(v_last())
        else:
            last = float(v_last)

        if isinstance(v_last_last, FunctionType):
            last_last = float(v_last_last())
        else:
            last_last = float(v_last_last)

        result = self.s_o.pop()['operation'](last_last, last)
        self.s_n.push(str(result))
        # if operator:
        #     self.s_o.push(operator)

    def finish_run(self):
        operations_length = len(self.s_o.get())
        numbers_length = len(self.s_n.get())
        result = self.s_n.get_last()

        if numbers_length > 1 or operations_length > 0:
            for i in range(operations_length):
                if numbers_length == 1:
                    self.run_one_command()
                else:
                    self.run_command()
            result = self.s_n.get_last()

        elif operations_length == 1 and numbers_length == 1 and self.s_o.get_last()['value'] == '-':
            result = '{:s}{:s}'.format(self.s_o.get_last()['value'], self.s_n.get_last())

        if '.0' in str(result):
            result = int(float(result))
        print(result)
