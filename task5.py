# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

lst_str = input('Введите набор целых чисел через запятую без пробелов: ')

lst = list()
for num_str in lst_str.split(','):        
    if num_str.count('.') <= 1 and num_str.find('-') <= 0 and num_str.replace('.','').replace('-','').isdigit():
        lst.append(float(num_str))
    else:
        lst.clear()
        print('Неверное значение списка!', num_str, '- не число!')
        break

if len(lst) > 0:
    summ = 0.0
    for num in range(0, len(lst)):
        if (num + 1) % 2 > 0:
            summ = summ + lst[num]                
    print('Сумма чисел на нечётных позициях списка равна =', summ)
    

