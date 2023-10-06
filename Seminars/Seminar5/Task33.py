# Задача №33. Р
# Хакер Василий получил доступ к классному журналу и # хочет заменить все свои минимальные оценки на
# максимальные.
# Напишите программу, которая # заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change(array):
    if len(array) < 2:
        return array
    else:
        min_mark = min(array)
        max_mark = max(array)
        new_array = [min_mark if i == max_mark else i for i in array]
        return new_array
list_1 = [int(input('Введите оценки Василия: ')) for i in range(5)]
print(*change(list_1))

# Или:

def change(array):
    if len(array) < 2:
        return array
    else:
        min_mark = min(array)
        max_mark = max(array)
        new_array = [min_mark if i == max_mark else i for i in array]
        return new_array
list_1 = [4, 1, 3, 3, 3]
print(*change(list_1))

# Или:

lst = [4, 1, 3, 3, 3]
min_el = min(lst)
max_el = max(lst)
res = []
for el in lst:
    if el == max_el:
        res.append(min_el)
    else:
        res.append(el)
print(res)

# Или:

def recur(lst, res=[], min_el=min(lst), max_el=max(lst)):

    if len(lst) == 0:
        return res
    if lst[0] == max_el:
        res.append(min_el)
    else:
        res.append(lst[0])

    return recur(lst[1:])


print(recur(lst))