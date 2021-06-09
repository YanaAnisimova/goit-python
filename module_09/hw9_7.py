def normal_name(list_name):

    new_list_name = []
    for i in map(lambda name: name.capitalize(), list_name):
        new_list_name.append(i)

    return new_list_name


print(normal_name(["dan", "jane", "steve", "mike"]))
