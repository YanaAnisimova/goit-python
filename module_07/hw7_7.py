def data_preparation(list_data):
    new_list = []
    for i in list_data:
        i.sort()
        if len(i) > 2:
            new_list += i[1:-1]
        else:
            new_list += i
    new_list.sort(reverse=True)

    return new_list


print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))
