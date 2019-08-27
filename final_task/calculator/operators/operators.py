import string
import math

zero_operator = {
    'value': '',
    'priority': -1,
    'operation': None
}

list_numbers = string.digits + str('.')
letters = string.ascii_lowercase
list_words = ['sin', 'cos', 'log']
list_math_numb = ['pi', 'e']

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
    },
    'sin': {
        'value': 'sin',
        'priority': 4,
        'operation': lambda a: math.sin(a)
    },
    'pi': {
        'value': 'pi',
        'priority': 4,
        'operation': lambda: math.pi
    },
    'e': {
        'value': 'e',
        'priority': 4,
        'operation': lambda: math.e
    },
    'log': {
        'value': 'log',
        'priority': 4,
        'operation': lambda a: math.log(a)
    },
    'log10': {
        'value': 'log10',
        'priority': 4,
        'operation': lambda a: math.log10(a)
    },
}
