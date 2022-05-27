# Задание. Напишите программу,
# которая принимает на вход два числа и
# проверяет является ли одно число квадратом другого.




# from calendar import c
# from re import A
# from this import d


# def square(a,b):
#     if a == b**2:
#        print(f"число {а} является двадратом {b} ")
#     else:
#        print("число {a} не является квадратом {b} ")
# square(4,2)  


# Задание.Напишите программу,которая на вход принимает 5 чисел
# и находит максимальное из них.

def number(a,b,c,d,f):
   max = 0
   if (a > b) and (a > c) and (a > d) and (a > f):
        max = a
   elif (b > c) and (b > d) and (b > f):
        max = b
   elif (c > d) and (d > f):
        max = c
   elif (d > f):
        max = d
   else: 
        max = f

   print(f"max = {max}")

number(11,20,3,40,5)

