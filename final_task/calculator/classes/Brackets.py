class Brackets:
    def __init__(self, __input: str):
        self.__input = __input
        self.list = []

    def erase(self):
        self.__deep_find(self.__input)

        for i in range(len(self.list) - 1):
            old_val = self.list.pop()
            result = str(eval(old_val))
            self.__update_list(old_val, result)

        self.__input = self.list[0]

    @staticmethod
    def __is_begin_bracket(value):
        return bool(~value.find('('))

    def __deep_find(self, value: str):
        self.list.append(value)

        value_str = value[value.find('(') + 1: value.rfind(')')]
        print(value_str)

        if self.__is_begin_bracket(value_str):
            self.__deep_find(value_str)
        else:
            self.list.append(value_str)

    def __update_list(self, old, new):
        self.list = [val.replace('(' + old + ')', new) for val in self.list]
        pass

    def get(self):
        return self.__input


s = Brackets('(1+(((90-((-30+12))-12)))+9)')
s.erase()
print(s.get())
