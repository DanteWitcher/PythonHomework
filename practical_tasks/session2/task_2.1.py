#!/usr/bin/env python3
from functools import reduce
from typing import Optional, Set
import string


def task1(*arr_str) -> set:
    if not arr_str:
        return None

    result = set(arr_str[0])

    for word in arr_str:
        if word == arr_str[0]:
            continue
        else:
            result.intersection_update(set(word))

    return None if bool(result) is False else result


def task2(*args) -> Optional[Set[str]]:
    if not args:
        return None

    return set().union(*args)


def task3(*args) -> Optional[Set[str]]:
    if not args:
        return None

    sets = [set(item) for item in args]

    result = {}

    for item in sets:
        for char in item:
            result[char] = result.get(char, 0) + 1
    return {key for key in result if result[key] > 1}


def task4(*args) -> Optional[Set[str]]:
    if not args:
        return None

    union_set = set().union(*args)
    alphabet_set = set(string.ascii_lowercase)

    return alphabet_set.difference(union_set)


input_string = ["hello", "world", "python", ]

print(task1(*input_string))
print(task2(*input_string))
print(task3(*input_string))
print(task4(*input_string))
