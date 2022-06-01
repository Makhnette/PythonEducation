# Задача №5 к 3-му ДЗ. Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
import csv

lst = list()
f = open('numbers.txt', 'r')
for str in f.read().split(','):
    if str.isdigit():
        lst.append(int(str))

print('numbers list:', lst)

for val in lst:
    if val % 2 == 0:
        lst.remove(val)

print('odd numbers lst only:',lst)