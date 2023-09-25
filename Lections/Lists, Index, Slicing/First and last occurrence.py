text = input('Введите слово: ')


try:
    first_occurrence = text.index('f')
    last_occurrence = text.rindex('f')
    print(first_occurrence if first_occurrence == last_occurrence else (first_occurrence, last_occurrence))
except ValueError:
    pass