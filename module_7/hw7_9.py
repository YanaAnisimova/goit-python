def all_sub_lists(data):

    new_list = [[]]

    for i in range(len(data)):
        for j in range(len(data)-i):
            new_list.append(data[j:j+i+1])

    return new_list


print(all_sub_lists([4, 6, 1, 3]))
