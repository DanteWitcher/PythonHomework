def split_by_index(string: str, indexes: list) -> list:
    arr, index_def = [], 0

    for index in indexes:
        if string.find(string, index):
            arr.append(string[index_def: index])
            index_def = index

        if indexes[len(indexes) - 1] == index and len(string) > index:
            arr.append(string[index_def:])

    return arr


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))
