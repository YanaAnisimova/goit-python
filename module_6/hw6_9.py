def write_to_bin(path, user_info):

    result = []
    with open(path, 'wb') as file:
        for username, password in user_info.items():
            file.write(f'{username}:{password}\n')
    with open(path, 'rb') as file:
        for i in file.readlines():
            result.append(i.decode('utf-8').replace('\n', ''))

        return result
