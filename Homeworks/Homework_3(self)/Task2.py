# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример
# list_1 = [1, 2, 3, 4, 5]
# k = 6 # 5
list_1 = [1, 2, 3, 4, 5]
k = 6 # 5

"""
closest = None  # Изначально нет ближайшего элемента
min_dif = float('inf')  # Изначально бесконечно большая разница

for item in list_1:
    dif = abs(item - k)  # Разница между текущим элементом и k
    if dif < min_dif:
        closest = item
        min_dif = dif

print(closest)
"""

new_list = [abs(list_1[i]-k) for i in range(len(list_1))]
print(list_1[new_list.index(min(new_list))])
