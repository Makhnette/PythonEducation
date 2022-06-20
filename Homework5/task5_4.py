# Задание №4. Чисто для тренировки новый функций, ничего сложного. 
# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. 
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. 
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер,
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. 
# Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, 
# в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. 
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

langs = ['C', 'CSharp', 'Python', 'Java', 'Go', 'Fortran', 'Algol', 'Delphi', 'JS', 'Basic', 'Rust']

lst = list()
for i in range(0, len(langs)):
    lst.append(i + 1)

def get_word_points(str):
    sum = 0
    for ch in str:
        sum += ord(ch) - ord('A') + 1

    return sum

def function_one():
    res = list()
    for i in range(0, len(langs)):
        res.append((lst[i], langs[i].capitalize()))
    return res

def function_two(lst: list[(int, str)]):
    res = list()
    for pair in lst:
        pnts = get_word_points(pair[1])
        if pnts % pair[0] == 0:
            res.append((pnts, pair[1]))
    return res

l = function_one()
print(l,'\n===>\n',function_two(l))

