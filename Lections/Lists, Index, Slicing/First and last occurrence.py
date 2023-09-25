# Задача 1. "Первое и последнее вхождение"
# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите.

text = input('Введите слово: ')

try:
    first_occurrence = text.index('f')
    last_occurrence = text.rindex('f')
    if first_occurrence == last_occurrence:
        print(first_occurrence)
    else:
        print(first_occurrence, last_occurrence)
except ValueError:
    pass