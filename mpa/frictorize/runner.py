# def factorize(number):
#
#
#
# 12/2 6
# 6/2
# 6/2 3
# 3/2 -> 3/
#
#
# 12/2 6
# 6/2 3
# 3/2 3/3 1
# 2 2 3

divisor = 2
number = 9
while number != 1:
    if number % divisor == 0:
        print(divisor)
        number = number / divisor
    else:
        divisor += 1



