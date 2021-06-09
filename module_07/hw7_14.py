def to_indexed(start_file, end_file):

    with open(start_file, 'r') as file:
        counter = 0
        new_string = ''
        for line in file:
            new_string += str(counter) + ': ' + line
            counter += 1
    with open(end_file, 'w') as file:
        file.write(new_string)
