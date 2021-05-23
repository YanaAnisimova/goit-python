class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not str(employee_id).startswith('01'):
        raise IDException
    id_list.append(employee_id)
    return id_list
