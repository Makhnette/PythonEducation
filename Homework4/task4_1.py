# Задача №1. Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию.
from genericpath import exists
from os import remove
import random
from turtle import width


file_name = 'numbers.txt'

if exists(file_name):
    remove(file_name)

with open(file_name, 'w') as f:
    for i in range(0,100):
        f.write(str(random.randrange(1, 10000)) + '\n')
    f.close()

lst = list()
with open(file_name, 'r') as f:
    for line in f.readlines():
        num_str = line.replace('\n', '')
        if num_str.isdigit():
            lst.append(int(num_str))
    f.close()

lst.sort()
with open(file_name, 'w') as f:
    f.flush()
    for num in lst:
        f.write(str(num) + '\n')
    f.close()

