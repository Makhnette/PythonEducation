# Задание.Дано число.Проверить кратно ли оно 5 и 10 или 15,но не 30.
number_str = input('Введите целое число: ')
if number_str.isdigit():
    number = int(number_str)
    if (number % 10 == 0 or number % 15 == 0) and number % 30 > 0:
        print("Число кратно 5 и 10 или 15,но не 30") 
    else:
        print("Число НЕ соответствует условию: кратно 5 и 10 или 15,но не 30") 
else:
    print("Вы ввели не число!")









