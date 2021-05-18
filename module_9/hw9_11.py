from functools import reduce


def sum_numbers(numbers):

    return reduce((lambda x, y: x + y), numbers)


print(sum_numbers([3, 4, 6, 9, 34, 12]))
