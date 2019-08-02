def foo(arr: list) -> list:
    result_arr = []
    for value in arr:
        result = 1
        for same_value in arr:
            if value != same_value:
                result *= same_value
        result_arr.append(result)
    return result_arr


print(foo([3, 2, 1]))
