from math import sqrt


total_of_numbers = 25
simple_numbers_flags = [True] * total_of_numbers
simple_numbers_flags[0] = False
simple_numbers_flags[1] = False

for number_index in range(2, int(sqrt(total_of_numbers))+1):
    print(f"number index is: {number_index}")
    for flag_index in range (number_index*2, total_of_numbers, number_index):
        simple_numbers_flags[flag_index] = False

for index in range(total_of_numbers):
    print(index, "-", "simple" if simple_numbers_flags[index] == True else "not simple")

# simple_numbers_flags = [True] * number
# print(s