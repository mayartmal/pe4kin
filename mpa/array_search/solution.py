def array_search(array: list, array_length: int, target_value: int):
    for index in range(array_length):
        if array[index] == target_value:
            return index
    return -1




