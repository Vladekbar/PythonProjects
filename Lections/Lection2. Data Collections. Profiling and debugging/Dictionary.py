# Dictionary

'''
d = {} # create dict
d = dict() # alt. create dict

d['q'] = 'qwerty '
print(d)

d['w'] = 'werty '
print(d['w' ])
'''

# dictionary = {}
# dictionary = {'up': 'verh', 'left': 'levo', 'down': 'vniz', 'right': 'pravo'}
# print(dictionary)
# print(dictionary['right'])
# dictionary['left'] = 'eto'
#
# print(dictionary['left'])
# print(dictionary)
# v = dictionary # можно сохранить словарь в переменной
# print(v)
#
# del dictionary['up'] # удаление ключа
# print(v)
#
# for item in dictionary:
#     print('{}: {}')

'''
dictionary = {}
dictionary = {'up': 'verh', 'left': 'levo', 'down': 'vniz', 'right': 'pravo'}
# 
# if dictionary['up'] == 'levo':
#     del dictionary['up']
# print(dictionary)


# dictionary['left'] = 'eto'
#
# print(dictionary['left'])
# print(dictionary)
# v = dictionary # можно сохранить словарь в переменной
# print(v)
#
# del dictionary['up'] # удаление ключа
# print(v)
#
'''

'''
 dictionary = {}
 dictionary = {'up': 'verh', 'left': 'levo', 'down': 'vniz', 'right': 'pravo'}
 for i in dictionary:
     print('{}: {}'.format(i, dictionary[i]))
 del dictionary['up'] # Удаление ключа
 dictionary[895] = 98998 # Добавление ключа
 dictionary[895] = 98998
 print(dictionary)
 dictionary[12] = (1, 2, 3, 'boom')
 print(dictionary)
 for (k, v) in dictionary.items():
     print(k, v) # k - key (Ключ), v - value(Значение)
 print(dictionary.items()) # Вывод списка, где каждый элемент является кортежем.
'''