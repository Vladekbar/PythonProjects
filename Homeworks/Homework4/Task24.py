n = int(input('Введите количество кустов: '))
if n < 4:
    print('Для данного количества кустов программа подсчета максимального сбора не требуется.')
else:
    list_1 = [int(input('Введите количество ягод для %s-го куста: ' % (i+1))) for i in range(n)]
    list_max_yield = [] # Список для хранения значений  урожайности за подход модуля.

    for i in range(n):
        list_max_yield.append(list_1[i-2] + list_1[i-1] + list_1[i])
    if list_max_yield.index(max(list_max_yield)) != 0:
        print(f'Для сбора максимального количества ягод ({max(list_max_yield)}) подгоните модуль к {list_max_yield.index(max(list_max_yield))}-му кусту.')
    else:
        print(f'Для сбора максимального количества ягод ({max(list_max_yield)}) подгоните модуль к {n}му кусту.')