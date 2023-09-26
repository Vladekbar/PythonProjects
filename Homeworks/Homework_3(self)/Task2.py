# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример
# list_1 = [1, 2, 3, 4, 5]
# k = 6 # 5
list_1 = [1, 2, 3, 4, 5]

new_list = [abs(list_1[i]-k) for i in range(len(list_1))]
print(list_1[new_list.index(min(new_list))])
