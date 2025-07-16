

def insert_sort():
    pass


def choose_sort(array):
    for external_index in range(len(array)):
        for internal_index in range(external_index, len(array)):
            if array[internal_index] < array[external_index]:
                array[external_index], array[internal_index] = array[internal_index], array[external_index]
    return array

array_a = [4, 2, 1, 5, 3]
choose_sort(array_a)
print(array_a)