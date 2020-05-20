a = float(input('Введите старт: '))
b = float(input('Введите конец: '))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
day += 1
print(day)