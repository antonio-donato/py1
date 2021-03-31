import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def rounding(number_to_round):
#    rounded_number = 1
    last_decimal = int(str(number_to_round)[-1])
    numero_to_round_string = str(number_to_round)
    if last_decimal == 0 or 1 or 2:
        numero_to_round_string[-1] = "0"
    elif last_decimal == 3 or 4 or 5 or 6 or 7:
        numero_to_round_string[-1] = "5"
    else:
        numero_to_round_string[-1] = 0
        numero = int(numero_to_round_string[-2]) + 1
        numero_to_round_string[-2] = numero

    return float(numero_to_round_string)


num = 10.362
# print(num)
# print(round_up(num, 2))
print(rounding(10.37))

