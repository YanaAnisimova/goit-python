def decode(data):

    if data == []:
        return []

    elif type(data[1]) == int:
        a = data[0:1] * data[1]
        return list(a) + decode(data[2:])


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))
