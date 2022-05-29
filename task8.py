# Написать программу преобразования десятичного числа в двоичное
from ast import Str


number_str = input('Введите целое положительное десятичное число:')

if not number_str.isdigit():
    print('Вы ввели неверное число! а может это и вовсе не число?..')
else:
    num = int(number_str)
    bits_lst = list()
    while(num > 0):
        bits_lst.append(num % 2)
        num = num // 2

    str_binary = ''
    for bit in reversed(bits_lst):
        str_binary = str_binary + str(bit)
    print('Получили двоичное число:', int(str_binary))
    print('Ну или так:', bin(int(number_str)))


