# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
N = int(input('Введите число N: '))
res_degree = 0
degree = 0  # Инициализируем degree до цикла
while res_degree <= N:
    res_degree = 2 ** degree
    if res_degree > N:
        break
    else:
        degree += 1
        print(res_degree)