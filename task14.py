# Экстра задача №1 к 3-му ДЗ.
# Определите функцию, которая принимает римскую цифру в качестве аргумента и возвращает ее значение в виде числового десятичного целого числа. Вам не нужно проверять форму римской цифры.
# Современные римские цифры записываются путем выражения каждой десятичной цифры числа, которое должно быть закодировано отдельно, начиная с самой левой цифры. Таким образом, 1990 отображается "MCMXC" (1000 = M, 900 = CM, 90 = XC), а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). Римская цифра для 1666, "MDCLXVI", использует каждую букву в порядке убывания.
# Пример: имя_вашей_функции ('XXI') # должно вернуть 21

latin_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def GetIntFromLatin(roman : str):
    num = 0
    last_val = 1001
    for ch in roman:
        val = latin_numbers.get(ch)
        if val == 0:
            return 'wrong format'
        else:
            if last_val >= val:
                num += val
            else:
                num += val - last_val * 2
            last_val = val
    return num

roman_numbers = ['MCMXC', 'MMVIII', 'MDCLXVI', 'XXI', 'XLIV']
for rn in roman_numbers:
    print(rn, '=>', GetIntFromLatin(rn))
