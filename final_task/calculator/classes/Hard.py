hard_operators = ['sin', 'cos', 'log', 'log10', 'pow', 'abs', 'round']

dict_operators = {
    'sin': {
        'value': 'sin',
        'priority': 1,
        'operation': lambda a, b: a + b
    },
    'sub': {
        'value': '-',
        'priority': 1,
        'operation': lambda a, b: a - b
    },
    'mul': {
        'value': '*',
        'priority': 2,
        'operation': lambda a, b: a * b
    },
    'div': {
        'value': '/',
        'priority': 2,
        'operation': lambda a, b: a / b
    },
    'fdiv': {
        'value': '//',
        'priority': 2,
        'operation': lambda a, b: a // b
    },
    'mod': {
        'value': '%',
        'priority': 2,
        'operation': lambda a, b: a % b
    },
    'pow': {
        'value': '^',
        'priority': 3,
        'operation': lambda a, b: a ** b
    }
}


class Hard:
    def __init__(self, __input: str):
        self.__input = __input
        self.list = []

    @staticmethod
    def __is_begin_bracket(value):
        return bool(~value.find('('))

    @staticmethod
    def __is_hard(input_str):
        i = 0

        for val in hard_operators:
            if val in input_str:
                i += 1

        return True if i else False

    def erase(self):
        pass

    def __find(self):
        for val in hard_operators:
            if val in self.__input:
                return val

    def run(self):
        value = self.__find()

        from_begin = self.__input.find(value)
        begin = self.__input.

        count = 0
        for i in from_begin:
            if i == '(':
                count += 1


h = Hard('(2+cos(pi/2^1)+log(1*(4+2^2)+1,3^2)-1)')
print(h.run())
