def add_order(order, path):
    
    file = open(path, 'a')
    file.write(order + '\n')
    file.close()
    file = open(path, 'r')
    counter = 0
    for line in file:
        if line.endswith(':active\n'):
            counter += 1
    file.close()
    
    return counter

