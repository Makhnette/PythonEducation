# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

lst_str = input('Введите набор целых чисел через запятую без пробелов: ')

lst = list()
for num_str in lst_str.split(','):        
    if num_str.count('.') <= 1 and num_str.find('-') <= 0 and num_str.replace('.','').replace('-','').isdigit():
        lst.append(float(num_str))
    else:
        lst.clear()
        print('Неверное значение списка!', num_str, '- не число!')
        break

lst_len = len(lst)
if lst_len > 0:
    print('На входе имеем список чисел:', lst)
    mult_lst = list()
    for index in range(0, lst_len // 2 + lst_len % 2):
        mult_lst.append(lst[index] * lst[lst_len - 1 - index])
    print('Результат:',mult_lst)


