def write_and_get_employees(employee_list, path):

    file = open(path, 'w')
    for i in employee_list:
        for j in i:
            file.write(j+'\n')
    file.close()

    file = open(path, 'r')
    new_list = file.readlines()
    file.close()

    return new_list
