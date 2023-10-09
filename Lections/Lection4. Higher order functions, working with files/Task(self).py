# В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# Герерация
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
print([(i, i**2) for i in list_1 if i % 2 == 0])
#[(2, 4), (8, 64), (38, 1444)]

# Или через функцию с возвратом
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
list_2 = []
def generate(array):
    for i in array:
        if i % 2 == 0:
            list_2.append((i, i**2))
    return list_2

print(generate(list_1))
# [(2, 4), (8, 64), (38, 1444)]

# Или через вызов функции напрямую

list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
list_2 = []
def generate(array):
    for i in array:
        if i % 2 == 0:
            list_2.append((i, i**2))

generate(list_1) # Вызов функции напрямую. List_2 теперь изменен.
print(list_2)
# Вывод видоизмененного List_2. [(2, 4), (8, 64), (38, 1444)]