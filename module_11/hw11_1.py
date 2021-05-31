class Customer:

    def __init__(self, surname, id=1):
        self.id = id
        self.surname = surname

    def __add__(self, other):
        return self.id + other.id
