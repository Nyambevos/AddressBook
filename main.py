from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Incorrect phone number")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, old_phone, new_phone):
        obj_old_phone = self.find_phone(old_phone)
        index_old_phone = self.phones.index(obj_old_phone)

        self.phones[index_old_phone] = Phone(new_phone)

    def find_phone(self, phone):
        ph = list(filter(lambda ph: ph.value == phone, self.phones))

        if len(ph) < 1:
            return None

        return ph[0]


class AddressBook(UserDict):
    def add_record(self, record):
        self.data.update({record.name.value: record})

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)
