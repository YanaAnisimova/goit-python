from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):

    sum = 0
    getcontext().prec = signs_count
    for number in number_list:
        sum += Decimal(number)

    return sum / len(number_list)


print(decimal_average([3, 5, 77, 23, 0.57], 6))
