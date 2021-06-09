def get_employees_by_profession(path, profession):
    new_list = []
    with open(path, 'r') as file:
        list_employees = file.readlines()
    print(list_employees)
    for i in list_employees:
        if i.find(profession) != (-1):
            new_list.append(i)
    result = ' '.join(new_list).replace(' '+profession, '')

    return result.replace('\n', '')
