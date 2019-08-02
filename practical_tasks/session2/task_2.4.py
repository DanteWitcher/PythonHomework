def combine_dicts(*args) -> dict:
    result = {}
    for dict_input in args:
        for key, val in dict_input.items():
            result[key] = result.get(key, 0) + val
    return result


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
 # {'a': 300, 'b': 200, 'c': 300}

print(combine_dicts(dict_1, dict_2, dict_3))