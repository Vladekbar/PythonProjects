# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
s = input()
a = s.find('h')
b = s.rfind('h')
fragment_1 = s[:a]
fragment_2 = s[b+1:]
print(fragment_1 + fragment_2)
