from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    @property
    def name(self):
        return self.value


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Incorrect phone number")
        super().__init__(value)


    @property
    def phone(self):
        return self.value
    



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    pass


p = Phone("1234567890")
print(p.phone)