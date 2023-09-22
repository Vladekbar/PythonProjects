### О МЕТОДЕ  .count()

.count() - это метод, внутри которого реализуется алгоритм подсчета.

Алгоритм может быть представлен в виде функции:
```python
def custom_count(sequence, item):
    count = 0
    for element in sequence:
        if element == item:
            count += 1
    return count
```

### Операции со множествами

```python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
print(c)
u = a.union(b) # объединение повторяющихся значений + запись неповторяющихся
print(u) # {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # Пересечение, т. е.повторение повторяющихся значений
print(i) # {8, 2, 5}
dl = a.difference(b) # Из множества a вычитаем повторяемые элементы множествa b
print(dl) # {1, 3}
dr = b.difference(a)
print(dr) # {13, 21}
q = a.union(b).difference(a.intersection(b)) # порядок опишем ниже
print(q) # {1, 21, 3, 13}
```