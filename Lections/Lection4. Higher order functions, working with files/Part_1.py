def f(x):
    return x*x

print(f(2))
print(type(f))
# Сократим

def f(x):
    return x**2
a = f # Переменная может хранить в себе ссылку на функцию.
print(a(4))
print(type(a))
