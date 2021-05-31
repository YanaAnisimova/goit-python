class Customer:
    def __init__(self, surname, id=1):
        self.surname = surname
        self.id = id

    def __add__(self, b):
        return self.id + b.id

    def __repr__(self):
        return f'Customer("{self.surname}", {self.id})'

    def __str__(self):
        return f"customer id = {self.id} and surname is {self.surname}"
