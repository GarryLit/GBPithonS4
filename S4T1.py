# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

import math

def in_numb(s):
    while 1:
        num = (input (s))
        if num == '0' or num == '' :
            print('Число не должно быть равно нулю')
            continue
        else:    
            return num
            break
        
acc = int(in_numb('Укажите точность = '))
acc = acc + 2
pi = str(math.pi)[0:acc]
print(float(pi))


