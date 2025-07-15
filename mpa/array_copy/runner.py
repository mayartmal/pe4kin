import random

array_length = 10
array_A = [0] * array_length
array_B = [0] * array_length
for index in range(array_length):
    array_A[index] = random.randint(0,10)
for index in range(array_length):
    array_B[index] = array_A[index]

print(array_A)
print(array_B)