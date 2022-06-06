# Задача №2 к 3-му ДЗ. Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.

prec = 0.0001

pi = 3.0
prev_pi = 100
mult = 2
sign = 1
while(abs(prev_pi - pi) > prec):
    prev_pi = pi
    pi = pi + sign * 4 / ( mult * (mult + 1) * (mult + 2) )
    mult = mult + 2
    sign = -sign
print('pi =', pi)
