#  Задание № 2. Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 

from dataclasses import field


def get_victory_combinations():
    res = list[list[(int, int)]]()
    subres1 = list[(int, int)]()
    subres2 = list[(int, int)]()
    for i in range(0,3):
        res.append([(i, 0), (i, 1), (i, 2)])
        res.append([(0, i), (1, i), (2, i)])
        subres1.append((i, i))
        subres2.append((i, 2 - i))
    res.append(subres1)
    res.append(subres2)
    return res

combs = get_victory_combinations()

def check_field(field: list[list[int]]):
    if len(field) != 3:
        return False
    for line in field:
        if len(line) != 3:
            return False
    return True

def is_comb_done(field: list[list[int]], comb: list[(int, int)], side: int):
    for pos in comb:
        if field[pos[0]][pos[1]] != side:
            return False
    return True

def get_game_result(field: list[list[int]]):
    has_empty = False

    for line in field:
        for pos in line:
            if pos == 0:
                has_empty = True
                break
        if has_empty:
            break

    if not has_empty:
        return 0

    for comb in combs:
        if is_comb_done(field, comb, 1):
            return 1
        elif is_comb_done(field, comb, 2):
            return 2

    return -1

def print_field(field: list[list[int]]):
    matrix = '    1   2   3\n  ┌───┬───┬───┐\n'
    for line_num in range(0, len(field)):
        line_str = '  │ '
        for pos in field[line_num]:
            line_str += str(pos) + ' │ '
        matrix += line_str + '\n'
        if line_num == len(field) - 1:
            matrix += '  └───┴───┴───┘'
        else:
            matrix += '  ├───┼───┼───┤\n'
    print(matrix)
        
def input_player_position(field: list[list[int]]):
    stat_player_turn = False
    player_pos = [0, 0]
    while not stat_player_turn:
        pos_str = input('Введите позицию по вертикали и по горизонтали через запятую (нуперация с 1): ')
        pos_str = pos_str.replace(' ','')
        if pos_str.replace(',','').isdigit() and len(pos_str.split(',')) == 2:
            line_pos = int(pos_str.split(',')[0]) - 1
            x_pos = int(pos_str.split(',')[1]) - 1

            if field[line_pos][x_pos] == 0:
                player_pos = [line_pos, x_pos]
                stat_player_turn = True
            else:
                print('  Данная позиция уже занята!')
        else:
            print('  Неверно задана позиция!')       

    return player_pos; 

def get_opp_position(field: list[list[int]]):
    c = (2,2)
    if field[1][1] == 0:
        return (1,1)

    res_pos = (-1, -1)

    # помешать игроку закрыть линию
    for comb in combs:
        cnt = 0
        for pos in comb:
            val = field[pos[0]][pos[1]]
            if val == 1:
                cnt += 1
            elif val == 0:
                res_pos = pos

        if cnt == 2 and sum(res_pos) >= 0:
            return res_pos
        res_pos = (-1, -1)

    res_pos = (-1, -1)
    # пытаться закрыть свою
    for comb in combs:
        for pos in comb:
            val = field[pos[0]][pos[1]]
            if val == 1:
                res_pos = (-1, -1)
                continue
            elif val == 0:
                res_pos = pos

        if sum(res_pos) >= 0:
            break
        res_pos = (-1, -1)

    return res_pos

field = [[0,0,0],[0,0,0],[0,0,0]]

stat = -1
while stat < 0:
    print_field(field)

    pl_pos = input_player_position(field)
    field[pl_pos[0]][pl_pos[1]] = 1

    opp_pos = get_opp_position(field)
    field[opp_pos[0]][opp_pos[1]] = 2

    stat = get_game_result(field)
    if stat == 1:
        print('Победа!')
    elif stat == 2:
        print('Поражение!')
    elif stat == 0:
        print('Ничья!')
