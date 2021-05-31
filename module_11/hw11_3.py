class Employees:
    def __init__(self, surnames, group):
        self.surnames = surnames
        self.group = group
        self.employees_dict = {}
        for i in self.surnames:
            self.employees_dict[i] = self.surnames.index(i)

    def __setitem__(self, key, value):
        self.employees_dict[key] = value

    def __getitem__(self, item):
        return self.employees_dict[item]
