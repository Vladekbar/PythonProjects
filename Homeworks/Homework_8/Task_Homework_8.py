# Функция для внесения нового контакта
def add_contact():
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    phonebook[name] = {"Имя": name, "номер": number}
    print("Контакт успешно добавлен")


# Функция для изменения контакта
def edit_contact():
    name = input("Введите полное наименование контакта: ")
    if name in phonebook:
        number = input("Введите новый номер телефона: ")
        phonebook[name] = {"Имя": name, "номер": number}
        print("Контакт успешно изменен")
    else:
        print("Контакт не найден")


# Функция для удаления контакта из телефонной книги
def delete_contact():
    name = input("Введите полное наименование контакта: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")


# Головная функция
phonebook = dict()
while True:
        action = input(
            "\nВыберите действие:\n1 - Добавить контакт\n2 - Изменить контакт\n3 - Удалить контакт\n4 - Вывести список контактов\n5 - Выйти из приложения\n")
        if action == "1":
            add_contact()
        elif action == "2":
            edit_contact()
        elif action == "3":
            delete_contact()
        elif action == "4":
            if not phonebook:
                print("Ваша телефонная книга пуста")
            else:
                for name, data in phonebook.items():
                    print("{0}: {1}".format(name, data["номер"]))
        elif action == "5":
            print("Завершение работы")
            break
        else:
            print("Некорректно введен пункт. Повторите попытку.")