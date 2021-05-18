import re


def generator_numbers(string=""):

    n_list = string.split(' ')
    for i in n_list:
        if re.search('\d+', i):
            yield re.search('\d+', i)[0]


def sum_profit(string):
    amount = 0
    number_generator = generator_numbers(string)
    for i in number_generator:
        print(i)
        amount += int(i)
    return amount


print(sum_profit('The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.'))
