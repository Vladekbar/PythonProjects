# Dictionary

'''
d = {} # create dict
d = dict() # alt. create dict

d['q'] = 'qwerty '
print(d)

d['w'] = 'werty '
print(d['w' ])
'''

dictionary = {}
dictionary = {'up': 'verh', 'left': 'levo', 'down': 'vniz', 'right': 'pravo'}
print(dictionary)
print(dictionary['right'])
dictionary['left'] = 'eto'

print(dictionary['left'])
print(dictionary)
v = dictionary # можно сохранить словарь в переменной
print(v)

del dictionary['up'] # удаление ключа
print(v)

for item in dictionary:
    print('{}: {}')