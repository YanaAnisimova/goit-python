from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, name, record):
        self.data[name] = record


class Record:

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, phone, new_phone):
        self.phones[self.phones.index(phone)] = new_phone


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name


class Phone(Field):

    def __init__(self, phone):
        self.phone = phone
