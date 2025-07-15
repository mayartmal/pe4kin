
def is_simple(number):

    """
    determines if the number is simple or not
    :return: True if thr number is simple, False - otherwise
    """


    for divisor in range(number - 1, 1, -1):
        if number % divisor == 0:
            # print(number % divisor)
            print("number is not simple")
            return False
    print("number is simple")
    return True


    # input_number/
    #
    #
    # 3/3
    # 3/2
    # 3/1
    #
    #
    # 4/4
    # 4/3
    # 4/2
    # 4/1
