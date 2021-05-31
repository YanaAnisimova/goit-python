from collections import UserDict
from datetime import date
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


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def __add__(self, phone):
        return self.phones.append(phone)

    def __sub__(self, phone):
        return self.phones.remove(phone)

    def change_phone(self, phone, new_phone):
        self.phones[self.phones.index(phone)] = new_phone

    def days_to_birthday(self, date_birth=None):
        if date_birth:
            self.birthday = date_birth
            if self.birthday.value.replace(date.today().year) > date.today():
                quantity_day = self.birthday.value.replace(date.today().year) - date.today()
            else:
                quantity_day = self.birthday.value.replace(
                    date.today().year + 1) - date.today()
            return quantity_day.days
        else:
            return 'Birthday not specified.'


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
            raise ValueError(f'This phone number "{new_phone}" is not correct. Please enter a 10 or 12 digit phone number.')
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
            raise ValueError(f'Please enter your birthday in the format: "YYYY-MM-DD".')
        else:
            self.__value = new_date_birth


if __name__ == '__main__':
    try:
        name = Name('Yana')
        name_m = Name('Monica')
        name_a = Name('Asya')
        name_b = Name('Bob')
        name_g = Name('G')

        phone = Phone('1111111111')
        phone_m = Phone('22222222222')
        phone_a = Phone('333333333333')
        phone_b = Phone('4444444444')
        phone_g = Phone('5555555555')
        phone_g_2 = Phone('666666666666')
        phone_g_3 = Phone('7777777777')

        record = Record(name)
        record_m = Record(name_m)
        record_a = Record(name_a)
        record_b = Record(name_b)
        record_g = Record(name_g)

        record + phone
        record_m + phone_m
        record_a + phone_a
        record_b + phone_b
        record_g + phone_g
        record_g - phone_g
        record_g + phone_g_2
        record_g + phone_g_3

        bd = Birthday('1990-09-09')
        print(record.days_to_birthday(bd))
        print(record_m.days_to_birthday())

        book = AddressBook()

        book.add_record(name, record)
        book.add_record(name_m, record_m)
        book.add_record(name_a, record_a)
        book.add_record(name_b, record_b)
        book.add_record(name_g, record_g)

    except ValueError as error:
        print(error)

    for i in book.iterator(1):
        print(f'\n name: {i[0].name.value}, phones: {[phone.value for phone in i[0].phones]}, birthday: {i[0].birthday.value if i[0].birthday else None}')
    # try:
    #     bd = Birthday('1990-10-11')
    #     name = Name('Yana')
    #     phone = Phone('096-600-63-00')
    #     record = Record(name)
    #     record.days_to_birthday(bd)
    #     phone_2 = Phone('1111111111')
    #     record.add_phone(phone_2)
    #     record.add_phone(phone)
    #     name.value = 'Valya'
    #     phone_2.value = '22222222222'
    #     bd.value = '1991-11-11'
    #     print(record.birthday.value)
    #     print(record.days_to_birthday(bd))
    #     print(record.phones)
    #     print(name.value)
    # except ValueError as error:
    #     print(error)





