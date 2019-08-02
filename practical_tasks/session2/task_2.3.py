def count_letters(input_string: str) -> dict:
    result = {}

    for letter in input_string:
        result[letter] = result.get(letter, 0) + 1

    return result


print(count_letters("stringsample"))