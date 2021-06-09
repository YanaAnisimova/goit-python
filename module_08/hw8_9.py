def modify_lists(list_for_dict, pow_dict, list_for_list, add_num):

    modified_dict = {id: id**pow_dict for id in list_for_dict}
    modified_list = [id+add_num for id in list_for_list]

    return modified_dict, modified_list


print(modify_lists([1, 3], 2, [3, 5], 7))
