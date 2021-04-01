import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def rounding(number_to_round):
#    rounded_number = 1
    last_decimal = int(str(number_to_round)[-1])

    if last_decimal in {0, 1, 2}:
        number_to_round = ((number_to_round * 100) - last_decimal) / 100
    elif last_decimal in {3, 4, 5, 6, 7}:
        number_to_round = ((number_to_round * 100) + (5 - last_decimal)) / 100
    else:
        number_to_round = ((number_to_round * 100) + (10 - last_decimal)) / 100

    return number_to_round


# num = 10.362
# print(rounding(10.33))
# print(rounding(10.37))
# print(rounding(10.39))
# print(rounding(10.32))

