import random

n = int(input('Введите длину списка: '))
m1 = int(input('Введите значение поиска ОТ: '))
m2 = int(input('Введите значение поиска ДО: '))

array = [0] * n

for i in range(n):
    array[i] = random.randint(0, 10)

for obj in array:
    if obj >= m1 and obj <= m2:
       print(obj)
