def inverse(array: list, array_length: int):
    for index in range(array_length // 2):
        array[index], array[array_length - 1 - index] = array[array_length - 1 - index], array[index]
    return array
