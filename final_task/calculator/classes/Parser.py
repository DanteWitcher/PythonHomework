from ..operators.operators import dict_operators, list_words, \
    list_numbers, list_operators, zero_operator, list_brackets, letters, list_math_numb
from .Stack import Stack
from .Executer import Executer


last_added_char = {
    # number, operator, bracket
    'last': '',
    'word': ''
}

stack_numbers = Stack()
stack_operations = Stack()

class Parser:
    def __init__(self, input_string: str):
        self.input = input_string
    # ( ( (22-33+3) -12)+1)

    def parse(self) -> None:
        for char in self.input:

            # LASTED IS EMPTY
            if last_added_char['last'] == '':
                operator = self.__find_operator(char)

                # CHAR IS NUMBER
                if self.__is_number(char):
                    stack_numbers.push(char)
                    last_added_char['last'] = 'number'

                # CHAR IS OPERATOR
                elif self.__is_operator(char) and char in '+-':
                    operator['is_unary'] = True
                    stack_operations.push(operator)
                    last_added_char['last'] = 'operator'

                # CHAR IS BRACKET
                elif self.__is_bracket(char):
                    self.__remove_brackets(operator)
                    last_added_char['last'] = 'bracket'

                # CHAR IS LETTER
                elif self.__is_word(char):
                    if last_added_char['word'] in list_words or last_added_char['word'] in list_math_numb:
                        stack_operations.push(self.__find_word(last_added_char['word']))
                    else:
                        last_added_char['word'] += char
                    last_added_char['last'] = 'letter'

                continue

            # LASTED IS NUMBER
            elif last_added_char['last'] == 'number':
                operator = self.__find_operator(char)

                # CHAR IS NUMBER
                if self.__is_number(char):
                    stack_numbers.concat_last_with(char)
                    last_added_char['last'] = 'number'

                # CHAR IS OPERATOR
                elif self.__is_operator(char):
                    self.__check_priority(operator)
                    # TO DO check
                    # stack_operations.push(self.__find_operator(char))
                    last_added_char['last'] = 'operator'

                # CHAR IS BRACKET
                elif self.__is_bracket(char):
                    if char == '(':
                        print('ERROR: '(' cant be before number: {}'.format(stack_operations.get_last())))
                    else:
                        self.__remove_brackets(operator)
                        last_added_char['last'] = 'bracket'

                # CHAR IS LETTER
                elif self.__is_word(char):
                    if char in list_math_numb:
                        stack_numbers.push(self.__find_word(char)['operation'])
                    else:
                        last_added_char['word'] += char
                    last_added_char['last'] = 'letter'

                continue

            # LASTED IS OPERATOR
            elif last_added_char['last'] == 'operator':
                operator = self.__find_operator(char)

                # CHAR IS OPERATOR
                if self.__is_operator(char) and char in '+-':
                    operator['is_unary'] = True
                    stack_operations.push(operator)

                # CHAR IS BRACKET
                elif self.__is_bracket(char):
                    if char == ')':
                        print('ERROR: '(' cant be before operator: {}'.format(stack_operations.get_last())))
                    else:
                        stack_operations.push(operator)
                        last_added_char['last'] = 'bracket'

                # CHAR IS NUMBER
                elif self.__is_number(char):
                    if char == ')':
                        print('ERROR: '(' cant be before operator: {}'.format(operator)))
                    else:
                        last_operator = stack_operations.get_last() or zero_operator
                        stack_numbers.push(char)

                        while last_operator.get('is_unary'):
                            last_number = stack_numbers.get_last()
                            if last_operator['value'] == '-' and '-' not in str(last_number):
                                stack_numbers.overwrite_last('-{:s}'.format(last_number))
                            elif last_operator['value'] == '-' and '-' in str(last_number):
                                stack_numbers.overwrite_last(str(last_number[1]))
                            elif last_operator['value'] == '+' and '-' in str(last_number):
                                stack_numbers.overwrite_last('{:s}'.format(last_number))
                            elif last_operator['value'] == '+' and '-' not in str(last_number):
                                stack_numbers.overwrite_last(str(last_number))
                            stack_operations.pop()
                            last_operator = stack_operations.get_last() or zero_operator

                        last_added_char['last'] = 'number'

                # CHAR IS LETTER
                elif self.__is_word(char):
                    if char in list_math_numb:
                        stack_numbers.push(self.__find_word(char)['operation'])
                    else:
                        last_added_char['word'] += char
                    last_added_char['last'] = 'letter'

                continue

            # LASTED IS BRACKET
            elif last_added_char['last'] == 'bracket':
                operator = self.__find_operator(char)

                # CHAR IS NUMBER
                if self.__is_number(char):
                    stack_numbers.push(char)
                    last_added_char['last'] = 'number'

                # CHAR IS OPERATOR
                elif self.__is_operator(char):
                    if stack_operations.get_last()['value'] == '(':
                        operator['is_unary'] = True
                    stack_operations.push(operator)
                    last_added_char['last'] = 'operator'

                # CHAR IS BRACKET
                elif self.__is_bracket(char):
                    self.__remove_brackets(operator)
                    last_added_char['last'] = 'bracket'

                # CHAR IS LETTER
                elif self.__is_word(char):
                    if char in list_math_numb:
                        stack_numbers.push(self.__find_word(char)['operation'])
                    else:
                        last_added_char['word'] += char
                    last_added_char['last'] = 'letter'

                continue

            # LASTED IS LETTER
            elif last_added_char['last'] == 'letter':
                operator = self.__find_operator(char)

                # CHAR IS NUMBER
                if self.__is_number(char):
                    stack_numbers.push(char)
                    print("ERROR: blaaa")
                    last_added_char['last'] = 'number'

                # CHAR IS OPERATOR
                elif self.__is_operator(char):
                    # if last_added_char['word'] in list_math_numb or last_added_char['word'] in list_words:
                    stack_operations.push(operator)
                    # else:
                    #     print('ERROR')
                    last_added_char['last'] = 'operator'

                # CHAR IS BRACKET
                elif self.__is_bracket(char):
                    if char == '(':
                        stack_operations.push(operator)
                    else:
                        stack_operations.push(operator)
                        print('ERROR')
                    last_added_char['last'] = 'bracket'

                # CHAR IS LETTER
                elif self.__is_word(char):
                    last_added_char['word'] += char

                    if last_added_char['word'] in list_words:
                        stack_operations.push(self.__find_word(last_added_char['word']))
                        last_added_char['word'] = ''
                    elif last_added_char['word'] in list_math_numb:
                        stack_numbers.push(dict_operators[last_added_char['word']]['operation'])
                        last_added_char['word'] = ''
                    last_added_char['last'] = 'letter'

                continue

        Executer(stack_numbers, stack_operations).finish_run()

    @staticmethod
    def __find_operator(char):
        for operator in dict_operators.values():
            if operator['value'] == char:
                return operator.copy()

    @staticmethod
    def __is_number(value) -> bool:
        return value in list_numbers

    @staticmethod
    def __is_operator(value) -> bool:
        return value in list_operators

    @staticmethod
    def __is_bracket(value) -> bool:
        return value in list_brackets

    @staticmethod
    def __is_word(value) -> bool:
        return value in letters

    @staticmethod
    def __remove_brackets(operator) -> bool:
        if operator['value'] == ')':
            last_operator = stack_operations.get_last() or zero_operator

            while last_operator['value'] != '(' and last_operator['priority'] != -1:
                Executer(stack_numbers, stack_operations).run_command()
                last_operator = stack_operations.get_last() or zero_operator

            stack_operations.pop()

        else:
            stack_operations.push(operator)

    def __check_priority(self, operator):
        last_operator = stack_operations.get_last() or zero_operator
        if last_operator['priority'] >= operator['priority'] and self.__is_operator(operator['value']):
            Executer(stack_numbers, stack_operations).run_command()
            self.__check_priority(operator)
        else:
            stack_operations.push(operator)

    @staticmethod
    def __find_word(word):
        return dict_operators['{:s}'.format(word)].copy()


