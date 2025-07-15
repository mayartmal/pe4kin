def factorize(number):
    factors = []
    divisor = 2
    while number != 1:
        if number % divisor == 0:
            factors.append(divisor)
            # print(divisor)
            number = number / divisor
        else:
            divisor += 1
    return factors




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