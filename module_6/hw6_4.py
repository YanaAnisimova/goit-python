def navigate_clients(path, code):

    file = open(path, 'r')
    file.seek(len(code)+1)
    first_line = file.readline()
    file.close()
    
    return first_line