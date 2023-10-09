def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

calc1 = lambda a,b: a + b

math(calc1, 5, 45)

# Вывод без calc1

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(lambda a,b: a + b, 5, 45)