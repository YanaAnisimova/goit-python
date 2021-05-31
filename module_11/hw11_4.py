class Employees:
    def __init__(self, surnames, group):
        self.employees_dict = {}
        ids = range(0, len(surnames))
        for iterator in range(0, len(surnames)):
            self.employees_dict[surnames[iterator]] = ids[iterator]
        self.group = group

    def __setitem__(self, key, value):
        self.employees_dict[key] = value

    def __getitem__(self, item):
        return self.employees_dict[item]

    def __call__(self, item):
        return [i for i, j in self.employees_dict.items() if item == j]
