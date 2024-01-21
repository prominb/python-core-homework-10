from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):  # Реалізовано валідацію номера телефону (має бути 10 цифр).
    def __init__(self, value):
        super().__init__(value)


class Record:
    '''Record: Додавання телефонів. Видалення телефонів. Редагування телефонів. Пошук телефону.'''
    def __init__(self, name):
        self.name = Name(name)  # Реалізовано зберігання об'єкта Name в окремому атрибуті.
        self.phones = []  # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    # Реалізовано методи для:
    def add_phone(self, phone: str):  # додавання - add_phone
        self.phones.append(Phone(phone))

    def remove_phone(self):  # видалення - remove_phone
        pass

    def edit_phone(self):  # редагування - edit_phone
        pass

    def find_phone(self):  # пошуку об'єктів Phone - find_phone
        pass


class AddressBook(UserDict):
    '''AddressBook: Додавання записів. Пошук записів за іменем. Видалення записів за іменем.'''
    """Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value."""
    # Реалізовано метод add_record, який додає запис до self.data.
    def add_record(self, record: Record):  # Додавання запису.
        self.data[record.name.value] = record

    def find(self):  # Реалізовано метод find, який знаходить запис за ім'ям.
        pass

    def delete(self):  # Реалізовано метод delete, який видаляє запис за ім'ям.
        pass


# Після реалізації ваш код має виконуватися наступним чином:

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
# print(john_record)
john_record.add_phone("1234567890")
# print(john_record)
john_record.add_phone("5555555555")
# print(john_record)
# print(john_record.__str__())

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
