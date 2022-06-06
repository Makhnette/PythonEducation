# Экстра - задача №2. Создать функцию, которая из списка чисел возвращает число, 
# являющее суммой двух или нескольких других элементов, либо возвращающее None, если такого числа нет.
from lib2to3.pytree import Node
from operator import indexOf
import random
from tkinter.messagebox import NO

def remove_in_position(lst: list, pos: int):
    res = list()
    for i in range(0, len(lst)):
        if(i != pos):
            res.append(lst[i])
    return res

def get_full_sum_lst(val: int, lst_sum: list[int], lst: list[int]):
    if val < 0:
        return None
    for i in range(0, len(lst)):
        val_next = val - lst[i]
        if val_next == 0:
            if len(lst_sum) > 0:
                lst_sum.append(lst[i])
                return lst_sum
            else:
                continue
        elif val_next < 0:
            continue
        else:
            lst_sum.append(lst[i])
            return get_full_sum_lst(val_next, lst_sum, remove_in_position(lst, i))

    return None

def get_num_sum_in_lst(lst: list[int]):
    for i in range(0, len(lst)):
        sub_lst = remove_in_position(lst, i)
        sub_res = get_full_sum_lst(lst[i], list(), sub_lst)
        if sub_res != None:
            print('found:', sum(sub_res), 'is summ of:', sub_res) # just for debug purpuses
            return sum(sub_res)

    return None

lst = list()
for i in range(1,10):
    lst.append(random.randrange(1,10))

# lst = [8, 8, 6, 6, 2, 6, 9, 5, 7]
print('Searching in', lst)
res = get_num_sum_in_lst(lst)
if res == None:
    print('No such number')
else:
    print('Number = ', res)
