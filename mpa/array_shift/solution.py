# def right_shift(array: list, length: int):
#     for index in range(length-1):
#         if index == 0:
#             backup_value, array[index], array[index + 1] = array[index + 1], array[length-1], array[index]
#         elif index == length - 2:
#             array[index + 1] = backup_value
#         else:
#             backup_value, array[index + 1] = array[index + 1], backup_value
#     return array

def right_shift(array: list, length: int):
    end_value = array[length-1]
    for index in range(length-1, 0, -1):
        array[index] = array[index - 1]
    array[0] = end_value
    return array




def left_shift(array: list, length: int):
    first_value = array[0]
    for index in range(length-1):
        array[index] = array[index + 1]
    array[length - 1] = first_value
    return array


