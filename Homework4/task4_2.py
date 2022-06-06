# # Задача №2. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую 
# последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]

import random

def get_ordered_lsts(prev_lst: list[int], lst: list[int]):
    res = list[list[int]]()

    for i in range(0, len(lst)):
        if len(prev_lst) == 0 or prev_lst[len(prev_lst) - 1] < lst[i]:
            next_lst = list(prev_lst)
            next_lst.append(lst[i])
            if len(lst) <= 1:
                res.append(next_lst)
            else:
                lst_rest = lst[i + 1: len(lst)]
                lsts = get_ordered_lsts(next_lst, lst_rest)
                for l in lsts:
                    res.append(l)
    if len(res) == 0:
        return [prev_lst]
    else:
        return res

lst = list()
for i in range(1,10):
    lst.append(random.randrange(1,100))

lst = [58, 19, 74, 23, 40, 80, 55, 76, 27]
lst_variants = get_ordered_lsts([], lst)

lst_res = list()
for loc_lst in lst_variants:
    if len(lst_res) < len(loc_lst):
        lst_res = list(loc_lst)

print(lst, '=>', lst_res)