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