from .Stack import Stack


class Executer:
    def __init__(self, stack_numbers: Stack, stack_operators: Stack):
        self.s_n = stack_numbers
        self.s_o = stack_operators

    def run_command(self):
        last = float(self.s_n.pop())
        last_last = float(self.s_n.pop())
        result = self.s_o.pop()['operation'](last_last, last)
        self.s_n.push(str(result))
        # if operator:
        #     self.s_o.push(operator)

    def finish_run(self):
        operations_length = len(self.s_o.get())
        numbers_length = len(self.s_n.get())
        result = self.s_n.get_last()

        if numbers_length > 1:
            for i in range(operations_length):
                self.run_command()
            result = self.s_n.get_last()

        elif operations_length == 1 and numbers_length == 1 and self.s_o.get_last()['value'] == '-':
            result = '{:s}{:s}'.format(self.s_o.get_last()['value'], self.s_n.get_last())

        if '.0' in str(result):
            result = int(float(result))
        print(result)
