# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и вывести многочлен степени k.

from random import randint

k= int(input("Введите степень к = "))
for i in range(k, 0, -1):
    koef = randint(1, 101)
    if koef == 1:
        koef = ''
    else:
        if i != 1:
            koef = f'{koef}*x^{i} +'
        else:
            koef = f'{koef}*x +'
    print(koef, end=' ')
print(f'{randint(1, 101)} = 0')