"""
Задача №113. Список квадратов


Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.

Входные данные
Задано единственное целое число N

Выходные данные
Необходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа
"""

n = 15
i = 1
while i**2 < n:
    print(i**2)
    i += 1