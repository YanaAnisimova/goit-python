from collections import UserDict
from datetime import date
import pickle
import re


class AddressBook(UserDict):
    def add_record(self, name, record):
        self.data[name] = record

    def iterator(self, n=None):
    # returns a view for 'n' records in one iteration
        outer_count = 1
        inner_count = 1
        n_records = []
        records = (i for i in self.data.values())
        for one_record in records:
            n_records.append(one_record)
            if inner_count == n or outer_count == len(self.data):
                yield n_records
                n_records = []
                inner_count = 0
            inner_count += 1
            outer_count += 1

    def save_dumped_data(self):
        with open('contact_list.txt', 'wb') as file:
            pickle.dump(self.data, file)

    def read_dumped_data(self):
        with open('contact_list.txt', 'rb') as file:
            self.data = pickle.load(file)
            return self


class Record:
    def __init__(self, name, birthday=None):
        self.name = name
        self.phones = []
        self.birthday = birthday

    def __add__(self, phone):
        self.phones.append(phone)
        return self

    def __sub__(self, phone):
        self.phones.remove(phone)
        return self

    def change_phone(self, phone, new_phone):
        self.phones[self.phones.index(phone)] = new_phone

    def days_to_birthday(self):
        if self.birthday:
            if self.birthday.value.replace(date.today().year) > date.today():
                quantity_day = self.birthday.value.replace(date.today().year) - date.today()
            else:
                quantity_day = self.birthday.value.replace(
                    date.today().year + 1) - date.today()
            return quantity_day.days
        else:
            return ''


class Field:

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_phone):
        REG_PHONE = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{3}[-\.\s]??\d{2}[-\.\s]??\d{2}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{2}[-\.\s]??\d{2})'
        if not re.search(REG_PHONE, str(new_phone)):
            raise ValueError(f'This phone number "{new_phone}" is not correct. Please enter a 10 or 12 digit phone number.\n')
        else:
            self.__value = new_phone

class Birthday(Field):
    # imput format: 'YYYY-MM-DD'
    def __init__(self, date_birth):
        self.value = date_birth

    @property
    def value(self):
        return date.fromisoformat(self.__value)

    @value.setter
    def value(self, new_date_birth):
        REG_DATE = r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
        if not re.search(REG_DATE, str(new_date_birth)):
            raise ValueError(f'Please enter your birthday in the format: "YYYY-MM-DD".\n')
        else:
            self.__value = new_date_birth
