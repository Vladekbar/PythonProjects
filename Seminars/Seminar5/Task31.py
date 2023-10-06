# Задача №31.
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
def fibonacci(n):
    if n <=1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

n = 7
print(fibonacci(7))