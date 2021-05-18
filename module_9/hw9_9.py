def positive_values(list_payment):

    return list(filter(lambda x: x > 0, list_payment))


print(positive_values([100, -3, 400, 35, -100]))
