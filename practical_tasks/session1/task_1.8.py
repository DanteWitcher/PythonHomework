#!/usr/bin/env python3
from functools import reduce


def get_pairs(arr: list) -> list:
    new_arr = []

    def do(a, b):
        new_arr.append((a, b))
        return b

    if len(arr) == 1:
        return None
    else:
        reduce(do, arr)
        return new_arr


print(get_pairs([1, 2, 3, 4]))
