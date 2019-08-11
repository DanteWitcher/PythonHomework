import string

zero_operator = {
    'value': '',
    'priority': -1,
    'operation': None
}

list_numbers = string.digits + str('.')
list_operators = ['+', '-', '*', '/', '//', '%', '^']
list_brackets = '()'

dict_operators = {
    'bracket_begin': {
        'value': '(',
        'priority': 0,
        'operation': None
    },
    'bracket_end': {
        'value': ')',
        'priority': 0,
        'operation': None
    },
    'add': {
        'value': '+',
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
