# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
coins = int(input('Quantity of coins? '))
coin_status = input('Write down the current status, for example hth mean head, teals, head: ')

if coins != len(coin_status):
    print('Error')
else:
    count_head = 0
    count_teals = 0
    for coin in coin_status:
        if coin =='h':
            count_head += 1
        else:
            count_teals += 1

print(f'Minimum number of flips - {min(count_head,count_teals)}')