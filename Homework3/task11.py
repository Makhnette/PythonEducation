# Задача №3 к 3-му ДЗ. Составить список простых множителей натурального числа N

n = 678878
simpl_lst = list()

num = n
val = 2
while val < num ** 0.5:
    while num % val == 0:
        num /= val
        simpl_lst.append(val)
    val += 1

if num != 1:
    simpl_lst.append(int(num))

print('Простые множители числа', n, ':', simpl_lst)
