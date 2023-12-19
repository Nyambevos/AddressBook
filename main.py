from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)


class Name(Field):
    def __init__(self, value):
        self.name = value

    @property
    def name(self):
        return self._value

    @name.setter
    def name(self, value):
        self._value = value


class Phone(Field):
    def __init__(self, value):
        self.phone = value

    @property
    def phone(self):
        return self._value

    @phone.setter
    def phone(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Incorrect phone number")
        self._value = value


class Birthday(Field):
    def __init__(self, value):
        self.birthday = value

    @property
    def birthday(self):
        return self._value

    @birthday.setter
    def birthday(self, value):
        if value is not None:
            self._value = datetime.strptime(value, "%d/%m/%Y")
        else:
            self._value = value


class Record:
    def __init__(self, name, birthday=None):
        self.__name = Name(name)
        self.__birthday = Birthday(birthday)
        self.__phones = []

    def __str__(self):
        name = self.__name.name
        phones = '; '.join(p.phone for p in self.__phones)
        birthday = self.__birthday.birthday
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
        index_old_phone = self.phones.index(obj_old_phone)

        self.__phones[index_old_phone] = Phone(new_phone)

    def find_phone(self, phone):
        ph = list(filter(lambda ph: ph.phone == phone, self.__phones))

        if ph:
            return ph[0]

        return None

    def days_to_birthday(self):
        if self.__birthday is not None:
            next_birthday = self.__birthday.birthday.replace(
                year=datetime.now().year)

            if next_birthday < datetime.now():
                next_birthday = next_birthday.replace(
                    year=next_birthday.year + 1)

            difference = next_birthday.date() - datetime.now().date()

            return difference.days

        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data.update({record.name.name: record})

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
