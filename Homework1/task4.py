# Задание.Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# объявим переменную строковую number_str и тут же заполним её 
# результатом метода input() ввода строки с терминала
number_str = input('Enter integer value N: ')

# проверим, что переменная number_str содержит в себе число, как мы просили
if number_str.isdigit():
    # если так, то приступим в цикле от 1 до введённого числа вычислять произведения
    # и записывать их в список (предварительно объявим объект lst типа list и
    # целочисленную переменную mult, которая будет каждый раз хранить текущее 
    # накопительное значение произведения чисел цикла),
    # естественно переменную number_str приведём к int
    lst = list()
    mult = 1
    for number in range(1, int(number_str) + 1):
        mult = mult * number
        lst.append(mult)
    
    # выведем содержимое заполненного списка в терминал
    print('Result list contsins', lst)

    