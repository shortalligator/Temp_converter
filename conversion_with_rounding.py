def round_ans(val):
    """
    Rounds temperatures to the nearest degree
    :param val:
    :return:
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    """
    Converts from °F to °C
    :param to_convert:
    :return:
    """
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_fahrenheit(to_convert):
    """
    Converts from °C to °F
    :param to_convert:
    :return:
    """
    answer = to_convert * 1.8 + 32
    return round_ans(answer)


# main routine
# to_c_test = [0, 100, -459]
# to_f_test = [0, 100, 40, -273]
#
# for item in to_c_test:
#     ans = to_fahrenheit(item)
#     print(f"{item}°C is {ans}°F")
#
# print()
#
# for item in to_c_test:
#     ans = to_celsius(item)
#     print(f"{item}°F is {ans}°C")
