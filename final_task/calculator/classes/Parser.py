from ..operators.operators import dict_operators, list_numbers, list_operators, zero_operator, list_brackets
from .Stack import Stack
from .Executer import Executer


last_added_char = {
    # number, operator, bracket
    'last': ''
}


stack_numbers = Stack()
stack_operations = Stack()

class Parser:
    def __init__(self, input_string: str):
        self.input = input_string
    # ( ( (22-33+3) -12)+1)
    def remove_brackets(self):
        first = self.input.split('(')

        if (len(last) - len(first)) != 1:
            print('ERROR: you have ')
            return None


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
                elif self.__is_operator(char):
                    # self.__check_priority(char)
                    stack_operations.push(operator)
                    last_added_char['last'] = 'operator'

                # CHAR IS BRACKET
                elif self.__is_bracket(char):
                    self.__remove_brackets(operator)
                    last_added_char['last'] = 'bracket'
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
                continue

            # LASTED IS OPERATOR
            elif last_added_char['last'] == 'operator':
                operator = self.__find_operator(char)

                # CHAR IS OPERATOR
                if self.__is_operator(char):
                    if operator['value'] == '+' and stack_operations.get_last()['value'] == '+':
                        stack_operations.overwrite_last(operator)
                    elif operator['value'] == '-' and stack_operations.get_last()['value'] == '+':
                        stack_operations.overwrite_last(dict_operators['sub'])
                    elif operator['value'] == '-' and stack_operations.get_last()['value'] == '-':
                        stack_operations.overwrite_last(dict_operators['add'])
                    else:
                        print('ERROR: you have two operators: {} and {} in your expression'
                              .format(stack_operations.get_last()['value'], operator['value']))

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
                        stack_numbers.push(char)
                        last_added_char['last'] = 'number'
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
                    if char in '+-':

                    stack_operations.push(operator)
                    last_added_char['last'] = 'operator'

                # CHAR IS BRACKET
                elif self.__is_bracket(char):
                    self.__remove_brackets(operator)
                    last_added_char['last'] = 'bracket'
                continue

            # for operator in dict_operators.values():
            #     if operator['value'] == char:
            #         if last_value['number'] is False:
            #
            #         else:
            #             self.__check_priority(operator)

        Executer(stack_numbers, stack_operations).finish_run()

        # for res in stack_numbers.get():
        #     print(res)
        #
        # for res in stack_operations.get():
        #     print(res['value'])

                # else:
                #     print('ERROR: pycalc does\'t know the char is {:s}'.format(char))
    @staticmethod
    def __find_operator(char):
        for operator in dict_operators.values():
            if operator['value'] == char:
                return operator

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
        # if selfx.__remove_brackets(operator) is True:
        #     last_value['bracket'] = True
        #     return

        if last_operator['priority'] >= operator['priority'] and self.__is_operator(operator['value']):

            Executer(stack_numbers, stack_operations).run_command()
            # last_operator = stack_operations.get_last() or zero_operator
            self.__check_priority(operator)
        else:
            stack_operations.push(operator)
