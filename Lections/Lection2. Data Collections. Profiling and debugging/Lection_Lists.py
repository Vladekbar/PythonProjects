# Срезы.

# Повторение
"""
list_1 = [4, 6, 66, 'privet']
list_1.append(3) # Добавили элемент в конце списка
print(list_1.insert(2, 11)) # Добавили элемент в третий индекс
list_1.pop(2) # Удалили элемент из третьего индекса
# print(list_1)
print(list_1[3])
"""

# CРЕЗЫ
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 'hey', 10]
print(list_1[0])
"""0"""
print(list_1[len(list_1)-1])
"""
1) Длина списка - 10 символов;
2) Действия в скобках [len(list_1)-1]: 10-9
3) print(list_1[len(list_1)-1]) = print(list_1[9]))
4) Выводим элемент под 9-м индексом. Это: 10
"""
print(list_1[-1])
"""
Отрицательная индексация. Первый элемент с конца.
Вывод: 10
"""
print(list_1[:])
print(list_1[:2])
print(list_1[2:])
# [:] - срез. Если ничего не стоит - выводит весь список.
"""[1, 2, 3, 4, 5, 6, 7, 8, 'hey', 10]"""
# [:2] - справа от ':x' -  выведи ДВА первых элемента.
"""[1, 2]"""
# [2:] - слева от 'x:' - выведи БЕЗ ДВУХ первых элементов.
"""[3, 4, 5, 6, 7, 8, 'hey', 10]"""
# Пример посложнее:
print(list_1[len(list_1)-2:])
"""10-2 --> print(list_1[8:] --> ['hey', 10]"""
print(list_1[2:9])
"""
2-й элемент не включительно, 9-й включительно
[3, 4, 5, 6, 7, 8, 'hey'] 
"""
print(list_1[-2:])
"""
['hey', 10]
Буквально: '-:' -  выведи последние '2' элемента 
"""
print(list_1[:-2])
"""
[1, 2, 3, 4, 5, 6, 7, 8]
Буквально: ':-' -  выведи БЕЗ ПОСЛЕДНИХ '2' элементов
"""
# Пример
print(list_1[-10:])
"""
Выведи последние 10 элементов. У нас их всего-то 10. Итог:
[1, 2, 3, 4, 5, 6, 7, 8, 'hey', 10]
"""
print(list_1[-20:])
"""
Да хоть -10000:, у нас не более 10 элементов. Итог:
[1, 2, 3, 4, 5, 6, 7, 8, 'hey', 10]
"""
print(list_1[:-10])
"""
Выведи без последних 10-ти элементов. Итог:
[]
"""
print(list_1[6:-2])
"""
Вспоминаем команды:
1) слева от 'x:' - выведи БЕЗ 6-ти первых элементов
2) ':-' -  выведи БЕЗ ПОСЛЕДНИХ '2' элементов.
Итог:
[7, 8]
"""
print(list_1[6:-4])
"""
1) слева от 'x:' - выведи БЕЗ 6-ти первых элементов
2) ':-' -  выведи БЕЗ ПОСЛЕДНИХ '4' элементов.
Итог =  не выведешь ничего, то есть:
[]
"""
print(list_1[0:])
# [0:] - слева от 'x:' - выведи БЕЗ 0 первых элементов.
"""[1, 2, 3, 4, 5, 6, 7, 8, 'hey', 10]"""
print(list_1[:0])
# [:0] - справа от ':x' -  выведи 0 первых элментов.
"""[]"""
print((list_1[0:len(list_1):6])) # [1, 7]
print((list_1[::6])) # [1, 7]
"""Оба случая: c начала до конца с шагом 6"""
print((list_1[1::6])) # [2, 8]
"""Выведи элемент [1] и [1 + 6] --> [1] и [7]"""
print((list_1[4::-2])) # [2, 8]
"""C [4] до конца с шагом -2""" # [5, 3, 1]
print((list_1[8:1:-2])) # ['hey', 7, 5, 3]


#Генератор списка