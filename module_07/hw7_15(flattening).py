def flatten(data):

    if data == []:
        return []
    elif type(data[0]) != list:
        new_list = []
        new_list.append(data[0])
        print(new_list)
        return new_list + flatten(data[1:])
    elif type(data[0]) == list:
        return flatten(data[0]) + flatten(data[1:])


print(flatten([1, 2, [3, 4, [5, 6]], 7]))
