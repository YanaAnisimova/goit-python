def make_request(keys, values):
    dictionary = {}
    if len(keys) == len(values):
        for i in range(len(keys)):
            dictionary[keys[i]] = values[i]

    return dictionary
