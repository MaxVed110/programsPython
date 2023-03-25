# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в
# задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import random

__all__ = ['eight_queens', 'random_placements']

QUEENS = 8


def eight_queens(queens_coord: list[list]):
    cord_x = [i[0] for i in queens_coord]
    cord_y = [i[1] for i in queens_coord]

    for i in range(QUEENS):
        for j in range(i + 1, QUEENS):
            if cord_x[i] == cord_x[j] or cord_y[i] == cord_y[j] or abs(cord_x[i] - cord_x[j]) == abs(
                    cord_y[i] - cord_y[j]):
                return False
    return True


def random_placements():
    res_dict = {}
    iter_ = 1
    glo = 0
    while len(res_dict.keys()) != 4:
        print(glo)
        coord_q = random_board()
        if eight_queens(coord_q):
            res_dict[iter_] = coord_q
            iter_ += 1
            print('app')
        glo += 1
    return res_dict


def random_board():
    board = [[random.randint(0, 8), random.randint(0, 8)] for i in range(QUEENS)]
    return board


if __name__ == '__main__':
    list_q = [[0, 0], [1, 5], [2, 7], [3, 2], [4, 6], [5, 3], [6, 1], [7, 4]]
    print(eight_queens(list_q))
    print(random_placements())
