from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.is_valid(value):
            self.__value = value

    def is_valid(self, value):
        return True


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value

    def is_valid(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Incorrect phone number")
        return True


class Birthday(Field):
    def __init__(self, value):
        self.value = self.date_conversion(value)

    def date_conversion(self, value):
        if value is not None:
            return datetime.strptime(value, "%d/%m/%Y").date()
        return None

    def is_valid(self, value):
        if value is not None:
            if value < datetime.now().date():
                return True


class Record:
    def __init__(self, name, birthday=None):
        self.__name = Name(name)
        self.__birthday = Birthday(birthday)
        self.__phones = []

    def __str__(self):
        name = self.__name.value
        phones = '; '.join(p.value for p in self.__phones)
        birthday = self.__birthday.value
        return f"Contact name: {name}, phones: {phones}, birthday: {birthday}"

    @property
    def name(self):
        return self.__name

    def add_phone(self, phone):
        self.__phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.__phones.remove(self.find_phone(phone))

    def edit_phone(self, old_phone, new_phone):
        obj_old_phone = self.find_phone(old_phone)

        if obj_old_phone is None:
            raise ValueError

        index_old_phone = self.__phones.index(obj_old_phone)

        self.__phones[index_old_phone] = Phone(new_phone)

    def find_phone(self, phone):
        ph = list(filter(lambda ph: ph.value == phone, self.__phones))

        if len(ph):
            return ph[0]

        return None

    def days_to_birthday(self):
        if self.__birthday is not None:
            next_birthday = self.__birthday.value.replace(
                year=datetime.now().year)

            if next_birthday < datetime.now().date():
                next_birthday = next_birthday.replace(
                    year=next_birthday.year + 1)

            difference = next_birthday - datetime.now().date()

            return difference.days

        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data.update({record.name.value: record})

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def __iter__(self):
        self.keys_records = list(self.data.keys())
        return self

    def __next__(self):
        if self.keys_records:
            return self.data[self.keys_records.pop()]
        raise StopIteration
