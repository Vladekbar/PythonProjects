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