# Address Book

This repository contains a simple implementation of an address book system in Python. It enables users to manage contacts with names and associated phone numbers.

## Getting Started

### Prerequisites

Ensure that you have Python installed on your machine. The code is compatible with Python 3.

### Usage

1. Clone the repository:

    ```bash
    https://github.com/Nyambevos/python-core-homework-10.git
    cd python-core-homework-10
    ```

## Code Structure

The code is organized into several classes:

- `Field`: Represents a generic field (e.g., name, phone).
- `Name`: Extends `Field` and represents a contact's name.
- `Phone`: Extends `Field` and represents a contact's phone number.
- `Record`: Represents a contact with a name and one or more phone numbers.
- `AddressBook`: Extends `UserDict` and represents the overall address book.

## Features

- **Add a Record**: Add a new contact to the address book.
- **Find a Record**: Retrieve contact information based on the name.
- **Delete a Record**: Remove a contact from the address book.
- **Add, Remove, and Edit Phones**: Manage phone numbers associated with a contact.


