#
## Множества

'''
colors = {'red', 'green', 'blue'}
# colors.add('red') # Добавление множества
print(colors)
colors.add('gray')
print(colors)
colors.remove('green') # Удаление множества
print(colors)
colors.discard('red') # discard проверит наличие 'red', если есть - удалит, если нет - пропустит без ошибки.
print(colors)
colors.clear() # Очистка множества set()
print(colors) # Вернет set()
q = set()
print(q) # Вернет set()
q = {'red', 'green', 'blue'} # Вернет {'blue', 'green', 'red'}
print(q)
'''

# Операции со множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
print(c)
u = a.union(b) # объединение повторяющихся значений + запись неповторяющихся
print(u) # {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # Пересечение, т. е.повторение повторяющихся значений
print(i) # {8, 2, 5}
dl = a.difference(b) # Из множества a вычитаем повторяемые элементы множествa b
print(dl) # {1, 3}
dr = b.difference(a)
print(dr) # {13, 21}
q = a.union(b).difference(a.intersection(b)) # порядок опишем ниже
print(q) # {1, 21, 3, 13}
'''
# Порядок выполнения
1) a.intersection(b) # {2, 5, 8}
2) a.union(b) # {1, 2, 3, 5, 8, 13, 21}
3) {1, 2, 3, 5, 8, 13, 21}  difference  {2, 5, 8} = {1, 3, 13, 21}
'''

# Замороженное множество

a = {1, 8, 6}

b = frozenset(a) # замороженное множество
print(b) # frozenset({8, 1, 6})