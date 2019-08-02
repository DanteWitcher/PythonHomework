def generate_squares(number: int) -> dict:
    result = dict()
    for i in range(number):
        value = i + 1
        result[value] = value * value

    return result


print(generate_squares(5))
