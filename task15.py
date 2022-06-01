# Экстра задача №2 к 3-му ДЗ.
# Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров комментариев. Любые пробелы в конце строки также должны быть удалены.
# Пример: 
# Входные данные:
# «apples, pears # and bananas
# grapes
# bananas !apples          » 
# Выходные данные:
# «apples, pears
# grapes
# bananas»
# Функция может вызываться вот так:
# result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

def CutOffComments(data_str : str, ch_lst : list[str]):
    res = ''
    for line in data_str.split('\n'):
        for ch in ch_lst:
            line = line.split(ch)[0]

        res += line.rstrip() + '\n'
    return res

in_str = "apples, pears # and bananas\n" + "grapes\n" + "bananas !apples          "
out_str = CutOffComments(in_str, ["#", "!"])
print(in_str + '\n'," ===> ", '\n' + out_str)