def evclid (a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
#
a = int(input('Введите значение А: '))
b = int(input('Введите значение B: '))

result = evclid(a, b)
print(result)
