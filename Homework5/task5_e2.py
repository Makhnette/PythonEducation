# Экстра-задача № 2.Единичная дробь имеет 1 в числителе. 
# Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:
# 1/2=0.5
# 1/3=0.(3)
# 1/4=0.25
# 1/5=0.2
# 1/6=0.1(6)
# 1/7=0.(142857)
# 1/8=0.125
# 1/9=0.(1)
# 1/10=0.1
# Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. 
# Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.

# Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр.
from decimal import Decimal
from tokenize import Double

def check_not_empty(val: str):
    if val == '':
        return False
    else:
        return True

def get_repat_part(s: str):
    for num_cha in range(0, len(s)):
        sub_world = s[:num_cha + 1]
        if len(s) > len(sub_world):
            last_s = s[num_cha + 1:]
            cnt = last_s.count(sub_world)

            if cnt == 0:
                continue

            f_str = last_s.replace(sub_world, '-')

            if len(f_str.replace('-','')) == 0:
                return sub_world

            f_lst = f_str.split('-')
            if '' in f_lst:
                f_lst = list(filter(check_not_empty, f_lst))

            if len(f_lst) == 1 and len(last_s) - cnt * len(sub_world) < len(sub_world):
                return sub_world

    return ''

part = get_repat_part(str(1 / Decimal(7))[2:])

lst = list()
for i in range(2, 1001):
    val = Decimal(1.0)
    val /= i
    s = str(val)[2:]
    part = get_repat_part(s)
    if part != '':
        lst.append((i, val, part))

max = (0, '')
for l in lst:
    if len(max[1]) < len(l[2]):
        max = (l[0], l[2])

print('1 / ', max[0], ':', max[1], 'len =', len(max[1]))
