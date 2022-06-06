# В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
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
    print('На входе имеем список чисел', lst)
    min_val = 1.0
    max_val = 0.0
    for val in lst:
        part_val = abs(val) - abs(val) // 1
        max_val = max(max_val, part_val)
        min_val = min(min_val, part_val)
    print('Разница между максимальной дробной частью числа из списка и минимальной:', 
    max_val - min_val)
