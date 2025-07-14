

def is_simple(input_number):

    """
    determines if the number is simple or not
    :return: True if thr number is simple, False - otherwise
    """


    for divisor in range(input_number-1, 1, -1):
        if input_number % divisor == 0:
            print(input_number % divisor)
            print("number is not simple")
            return
    print("number is simple")


is_simple(23)

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


