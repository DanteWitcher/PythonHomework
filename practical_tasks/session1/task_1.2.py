#!/usr/bin/env python3


def is_palindrome(input_string: str) -> str:
    for index in range(0, len(input_string) // 2):
        if input_string[index] != input_string[-(index + 1)]:
            return False
    return True


print('sassas:', is_palindrome('sassas'))
print('sasss: ', is_palindrome('sasss'))

