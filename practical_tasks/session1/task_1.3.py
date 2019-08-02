def split(input_string: str, separator: str) -> list:
    arr, index = [], 0

    while True:
        found_index = input_string.find(separator, index)

        if index == len(input_string):
            break
        elif found_index == -1:
            arr.append(input_string[index: len(input_string)])
            break
        elif separator == '':
            arr.append(input_string[index: found_index + 1])
            index = found_index + 1
        else:
            arr.append(input_string[index: found_index])
            index = found_index + len(separator)
    return arr


print(split('sasha you need tell your friend something', 'you'))
