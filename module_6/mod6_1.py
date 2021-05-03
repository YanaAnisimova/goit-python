def read_file(path):
    
    file = open(path)
    amount_of_proceeds = 0
    while True:
        line = file.readline()
        if not line:
            break
        proceeds = line.split()[1]
        amount_of_proceeds += float(proceeds)
    file.close()
    
    return amount_of_proceeds
