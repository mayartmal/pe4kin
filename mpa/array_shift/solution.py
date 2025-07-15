def right_shift(array: list, length: int):
    for index in range(length-1):
        if index == 0:
            backup_value, array[index], array[index + 1] = array[index + 1], array[length-1], array[index]
        elif index == length - 2:
            array[index + 1] = backup_value
        else:
            backup_value, array[index + 1] = array[index + 1], backup_value
    return array


def left_shift(array: list, length: int):
    first_value = array[0]
    for index in range(length):
        if index == length - 1:
            array[index] = first_value
        else:
            array[index] = array[index+1]
    return array