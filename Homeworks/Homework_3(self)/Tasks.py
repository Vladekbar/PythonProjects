list_1 = [1, 'man', 3, 3, 'man', 3]
k = 3
# count = 0
# for i in range((list_1)):
#     if list_1[i] == 'man':
#         count = count + 1
# print(count)
print(list_1.count(k))

"""
О МЕТОДЕ .count()
.count() - это метод, внутри которого реализуется алгоритм подсчета.

Алгоритм может быть представлен в виде функции):
def custom_count(sequence, item):
    count = 0
    for element in sequence:
        if element == item:
            count += 1
    return count
"""