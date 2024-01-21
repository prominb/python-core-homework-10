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
        self.value = self.check_phone(value)

    def check_phone(self, value):  # Реалізовано валідацію номера телефону (має бути 10 цифр).
        if len(value) == 10 and value.isdecimal():
            return value
        else:
            raise ValueError("Phone must contain 10 digits only!")


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

    def remove_phone(self, phone: str):  # видалення - remove_phone
        # pass
        for i in range(len(self.phones)):
            if str(self.phones[i]) == phone:
                return self.phones.pop(i)

    def edit_phone(self, phone: str, new_phone: str):  # редагування - edit_phone
        # pass
        is_exists = self.find_phone(phone)
        # print(f'XXXXX - {is_exists}')
        # print(self.phones.index(is_exists))
        # get_index = self.phones.index(is_exists)
        # print(f'Phone INDEX is {get_index}')
        if is_exists:
            get_index = self.phones.index(is_exists)
            self.phones[get_index] = Phone(new_phone)
        else:
            # print('BBBBBBBBBBBBBBBBBBBBBBBBB')
            raise ValueError(f'Phone {phone} not found!')
        # print(phone, self.phones[0], phone in self.phones, new_phone)
        # print(type(phone), type(str(self.phones[0])))
        # print(phone == str(self.phones[0]))
        # print(self.phones)
        # for i in range(len(self.phones)):
            # print(str(self.phones[i]) == phone)
            # if str(self.phones[i]) == phone:
            #     self.phones[i] = Phone(new_phone)
            #     break
            # else:
                # if str(self.phones[i]) != phone:
                # raise ValueError('GGGGGGGGGGGGGGGGGGGG')
                # else:
                    # not_exists = Phone(phone)
                    # self.phones[i] = not_exists
                # print(not_exists)
                # print('XXXXXXXXXXXXXXXXXXXXXXXX')
                # break
                # return self.phones.index(phone)
                # try:
                #     self.phones.index(phone)
                # except ValueError as vleerr:
                #     print(vleerr)
        # raise ValueError(f'Phone {phone} not found!')

    def find_phone(self, phone: str):  # пошуку об'єктів Phone - find_phone
        # pass
        for i in range(len(self.phones)):
            if str(self.phones[i]) == phone:
                return self.phones[i]
        # if phone in
        # return phone


class AddressBook(UserDict):
    '''AddressBook: Додавання записів. Пошук записів за іменем. Видалення записів за іменем.'''
    """Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value."""
    # Реалізовано метод add_record, який додає запис до self.data.
    def add_record(self, record: Record):  # Додавання запису.
        self.data[record.name.value] = record

    def find(self, name):  # Реалізовано метод find, який знаходить запис за ім'ям.
        return self.data.get(name)

    def delete(self, name):  # Реалізовано метод delete, який видаляє запис за ім'ям.
        # pass
        # print(name in self.data)
        if name in self.data:
            return f'Record with {self.data.pop(name)} was removed!'


# Після реалізації ваш код має виконуватися наступним чином:

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
# print(john_record)
john_record.add_phone("1234567890")
# print(john_record)
john_record.add_phone("5555555555")
# john_record.add_phone("5555555")
# print(john_record)
# john_record.add_phone("555qq55555")
# print(john_record)
# print(john_record.__str__())
# john_record.add_phone("6666666666")

# Додавання запису John до адресної книги
book.add_record(john_record)
# print(book)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
# jane_record.add_phone("98765432as")
book.add_record(jane_record)
# print(book)

# Виведення всіх записів у книзі
# for name, record in book.data.items():
    # print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
# john = book.find("Johnny")
print(john)
john.edit_phone("1234567890", "1112223333")
# john.edit_phone("5555555555", "1112223333")
# john.edit_phone("1234567890", "111222ww33")
# john.edit_phone("1234567890", "11122233")
# john.edit_phone("7777777777", "1112223333")
# john.edit_phone("77777e77", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
# found_phone = john.find_phone("5555555512")
# found_phone = john.find_phone("55555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення конкретного телефону у записі John
# delete_phone = john.remove_phone("5555555555")
# print(f"In Contact: {john.name} - Phone number {delete_phone} was removed.")  # Видалення: 5555555555

# john_record.add_phone("6666666666")
# print(john_record)

# Видалення запису Jane
book.delete("Jane")
# print(book.delete("Jane"))
# print(book.delete("Johnny"))

# print(john)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)
