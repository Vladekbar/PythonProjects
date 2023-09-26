# PythonStudy
## Строки и их методы.


&#9757; Важно! **Вызов метода** = Объект.Метод(аргументы)

* метод **.upper()** - все маленькие буквы превратит в большие.
* метод **.lower()** - все большие буквы превратит в маленькие.
* метод **.count()** - подсчитывает количество элементов.
* * *Пример*. В строке **s** необходимо найти некоторое количество символов 'o'.
* * s.count('o') - выдаст количество символов 'o' в строке s.
* * s.count('o',7) - выдаст количество символов 'o' в строке s c **седьмой позиции**.
* * s.count('o',3, 7) - ('что ищем', с какого индекса, по какой)
* метод **.find()** - ищет самый первый индекс элемента
* метод **.rfind()** - ищет самый последний индекс элемента
* * метод **.index()**  - то же, что и **.find()**, но выдает ошибку при отсутсвии элемента.
* метод **.replace()** - обязательно 2 параметра. ЧТО будем менять и НА ЧТО будем менять.
* * s.replace('.', '!')
* метод **.replace('.', '!', 2)**  - третий параметр. СКОЛЬКО замен я хочу сделать слева направо (2).
* метод **.isalfa()**  - проверяет, состоит ли строка из букв.
* метод **.isdigit()** - проверяет, состоит ли строка из цифр.
* метод **.rjust()** - дополняет строку до указанной длины, и при этом отодвигает значение вправо.

```python
s = '111'
s.rjust(5)
# '  111'
```
* метод **.ljust** - дополняет строку до указанной длины, и при этом отодвигает значение влево.
* метод **.split()**  - по умолчанию можно вызывать без параметров. Разбивает строку по пробелам.
* * Там, где он встречает пробел, он его удаляет, и все, что было до этого пробела - вырезает в отдельную строку и сохраняет в список.
```python
s = 'ivanov ivan ivanovich'
print(s.split())
# ['ivanov', 'ivan', 'ivanovich']
print(len(s.split())) # Подсчет количества слов
# 3
```
* * Можно разбить по букве 'n'.
```python
s = 'ivanov ivan ivanovich'
print(s.split('n'))
# ['iva', 'ov iva', ' iva', 'ovich']
```
* метод **.strip()** - вызов без параметра. Удаляет пробелы и переносы на новую строку. 
*  * Существуют разновидности **.rstrip()** и **.lstrip()**.

* метод **.join()** - используется для объединения (соединения) элементов последовательности (например, символов в строке) в одну строку.
**.join()** принимает последовательность (например, список, кортеж или строку) и вставляет указанную строку между элементами этой последовательности, после чего возвращает новую строку

### Примеры использования метода .join():

- Соединение элементов списка в одну строку:
```python
my_list = ['apple', 'banana', 'cherry']
result = ', '.join(my_list)
print(result)
# Вывод: "apple, banana, cherry"
```
- Cоединение символов строки с заданным разделителем:
```python
text = "Hello"
result = '-'.join(text)
print(result)
# Вывод: "H-e-l-l-o"
```
- Объединение чисел в строку:
```python
numbers = [1, 2, 3, 4, 5]
result = ''.join(map(str, numbers))
print(result)
# Вывод: "12345"
```


### Методы .split и .join вместе на практике на практике.

```python
s = '43,52,66,76'
print(s.split(',')) # Разделим по знаку запятой.
# Вывод: ['43', '52', '66', '76']
```
Теперь научимся соединять такие строки. Объединить список в строку обратно.

```python
s = '43,52,66,76'
t = s.split(',')
print('='.join(t))
# Вывод: 43=52=66=76
print('='.join(s.split(',')))
# Вывод: 43=52=66=76
```
## Задачи
### Задача 1. "Первое и последнее вхождение"
* Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. 
* Если она встречается два и более раз, выведите индекс её первого и последнего появления.
* Если буква f в данной строке не встречается, ничего не выводите.
```python
text = input('Введите слово: ')

try:
    first_occurrence = text.index('f')
    last_occurrence = text.rindex('f')
    if first_occurrence == last_occurrence:
        print(first_occurrence)
    else:
        print(first_occurrence, last_occurrence)
except ValueError:
    pass
```
**try, except, pass** - это элементы обработки исключений в Python. Вот как они работают:
<div style="text-align: justify;">

1) **try**: Ключевое слово try используется для определения блока кода, в котором может возникнуть исключение. Вы пишете код, который может вызвать исключение внутри блока try.


2) **except**: Ключевое слово except используется для указания, как обрабатывать исключение, которое может возникнуть внутри блока try. Вы можете указать определенный тип исключения (например, ValueError, TypeError, ZeroDivisionError) или использовать except без указания конкретного типа для обработки любых исключений, которые могут возникнуть.


3) **pass**: Ключевое слово pass используется внутри блока except, чтобы показать, что ничего не нужно выполнять, если исключение было обработано. Оно позволяет избежать ошибок синтаксиса, но не выполняет никаких дополнительных действий.
</div>

> &#9757; **Простыми словами**  
>Мы не уверены, что что-то произойдет, но попробуем. Если да - то так, если нет - ничего.
>Такая вот альтернатива многоэтажности конструкции **if**.

### Задача 2. Удаление фрагмента

* Дана строка, в которой буква h встречается минимум два раза. 
* Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

```python
s = input()
a = s.find('h')
b = s.rfind('h')
slice_1 = s[:a]
slice_2 = s[b+1:]
print(slice_1 + slice_2)
```
*Решение через срезы*. 
&#9757; **Конкатенация** - операция объединения или склеивания строк (или других последовательностей) в одну строку или последовательность.
* Осуществляется, например, как в нашей задаче через оператор **+**
* Также возможно через метод **str.join()**

Пример этой же задачи, решенной с помощью метода  **str.join()**.
```python
s = 'In the hole in the ground there lived a hobbit'
a = s.find('h')
b = s.rfind('h')
print("".join([s[:a], s[b+1:]]))
# In tobbit
```
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
*Порядок выполнения*
1) a.intersection(b) # {2, 5, 8}
2) a.union(b) # {1, 2, 3, 5, 8, 13, 21}
3) {1, 2, 3, 5, 8, 13, 21}  difference  {2, 5, 8} = {1, 3, 13, 21}

### Интересный пример

Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

```python
list_1 = [1, 2, 3, 4, 5]
k = 6 
```
Рассмотрим не менее интересное решение:

```python
new_list = [abs(list_1[i]-k) for i in range(len(list_1))]
print(list_1[new_list.index(min(new_list))])
```

При создании нового списка в квадратных скобках указан оператор for,
который обычно стоит где-то в начале, а в конце условия содержится двоеточие.

В данном контексте for выполняет итерацию по индексам элементов списка list_1.

*for* используется в генераторе списка, который создает новый список *new_list*. 
Генератор списка - это синтаксический сахар, который позволяет создавать новый список путем выполнения итерации 
по другому итерируемому объекту.В данном случае, по *range(len(list_1)))* и применения выражения 
(в данном случае, *abs(list_1[i]-k))* к каждому элементу.

Разберем по порядку на примерах.

1) Создание списка из генерируемых элементов:
```python
list_1 = [i for i in range(5)]
print(list_1)
```
>[0, 1, 2, 3, 4]

2) Заранее зададим условие, чтобы элементы видоизменялись по ходу итеррации.
```python
list_1 = [i+2 for i in range(5)]
print(list_1)
```
>[2, 3, 4, 5, 6]

Уже результат отличается.

5) А давайте добавим туда модуль, а сложение заменим вычитанием?
```python
list_1 = [abs(i-2) for i in range(5)]
print(list_1)
```
>[2, 1, 0, 1, 2]

Очень интересно! (И все понятно, не надо тут.)

Вернемся ко второй строке нашего кода.
```python
print(list_1[new_list.index(min(new_list))])
```
В общих черта понятно, что требуется вывести некий элемент.
```python
print(list_1['нечто страшное'])
```
Разберем 'нечто страшное'.
```python
new_list.index(min(new_list))
```
>min(new_list)

функция min вернет наименьшее значение элемента в списке.

>new_list.index(min(new_list))  

укажет индекс наименьшего элемента. 

Соответсвенно:


```python
print(list_1['укажет индекс наименьшего элемента'])
```

#### Выведет сам элемент.

### Чисто пример для упрощения понимания.

```python
l_1 = [i for i in range(1,6)]
print(l_1) # [1, 2, 3, 4, 5] # Вывод списка
print(min(l_1)) # 1 Вывод минимального элемента
print(l_1.index(max(l_1))) # 4 Вывод ИНДЕКСА максимального элемента
print(l_1[(l_1.index(max(l_1)))]) # 5 Вывод МАКСИМАЛЬНОГО элемента.

```
