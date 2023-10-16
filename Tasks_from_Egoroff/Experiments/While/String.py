s = 'spaKowwz12Kert'
print(s[0])
print(s[1:])
while len(s) > 0:
    print(s[0])
    s = s[1:]

g = 'spaKowwz12K,;rrk./5%ert'
while len(g) > 0:
    letter = g[0]
    if letter >= 'a' and letter <= 'z':
        print(letter, 'small')
    elif letter >= 'A' and letter <= 'Z':
        print(letter, 'capital')
    elif letter.isdigit():
        print(letter, 'digit')
    else:
        print(letter, 'other')
    g = g[1:]
