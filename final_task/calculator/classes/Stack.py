from typing import TypeVar, Generic, List


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.__stack = []

    def get(self):
        return self.__stack

    def push(self, value: T) -> None:
        self.__stack.append(value)

    def pop(self) -> T:
        return self.__stack.pop()

    def set(self, stack: List[T]) -> None:
        self.__stack = stack

    def clear(self) -> None:
        self.__stack = []

    def concat_last_with(self, number: T) -> None:
        self.__stack[len(self.__stack) - 1] = str(self.__stack[len(self.__stack) - 1]) + str(number)

    def get_last(self):
        if len(self.__stack) == 0:
            return None
        else:
            return self.__stack[len(self.__stack) - 1]

    def overwrite_last(self, val: T):
        if len(self.__stack) == 0:
            return None
        else:
            self.__stack[len(self.__stack) - 1] = val
