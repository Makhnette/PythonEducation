# Экстра задача №3 к 3-му ДЗ.
# Найдите максимальную сумму пути от вершины до основания следующего треугольника:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# it's time to make some recursion... pain
def GetSummLst(lst: list[list[int]], summ: int, curr_line: int, pos1: int, pos2: int):

    if pos1 >= len(lst[curr_line]) or pos2 >= len(lst[curr_line]) or pos2 < pos1:
        return [summ]

    if curr_line >= len(lst) - 1:
        return [summ]
    else:
        res = []
        for s in GetSummLst(lst, summ + lst[curr_line][pos1], curr_line + 1, pos1, pos1 + 1):
            res.append(s)
        for s in GetSummLst(lst, summ + lst[curr_line][pos2], curr_line + 1, pos2, pos2 + 2):
            res.append(s)
        return res

lst = list()
f = open('triangle.txt', 'r')
for line in f.read().split('\n'):
    line_lst = list()
    for num_str in line.split(' '):
        if num_str.isdigit():
            line_lst.append(int(num_str))
    lst.append(line_lst)

for line in lst:
    print(line)

summ_lst = GetSummLst(lst, lst[0][0], 1, 0, 1)
print('found', len(summ_lst), 'different path summs. Max summ =', max(summ_lst))


