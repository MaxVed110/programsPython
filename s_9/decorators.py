import csv
import json
import math
import random
from typing import Callable
from functools import wraps
from random import randint as ri


# Зад 1
def guess_number(number: int, count: int):
    counter = count

    def guess():
        nonlocal counter
        while counter > 0:
            n = int(input('Введите число: '))
            counter -= 1
            if n < number:
                print(f'Больше ост{counter}')
            if n > number:
                print(f'Меньше ост{counter}')
            if n == number:
                print('Победа')
                break
            if counter == 0:
                print('Конец')
                break

    return guess()


# Зад 2 + 6
def check(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 0 < args[0] < 101 and 0 < args[1] < 11:
            res = func(*args, **kwargs)
        else:
            res = func(random.randint(0, 100), random.randint(1, 10))
        return res

    return wrapper


@check
def guess(number: int, count: int):
    counter = count
    while counter > 0:
        n = int(input('Введите число: '))
        counter -= 1
        if n < number:
            print(f'Больше ост{counter}')
        if n > number:
            print(f'Меньше ост{counter}')
        if n == number:
            print('Победа')
            break
        if counter == 0:
            print('Конец')
            break


# Зад 3 + 6
def save_as_json(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res_and_param = {'Позиционные': [args],
                         'Результат': res}
        for k in kwargs:
            res_and_param[k] = 'ключевой'
        with open(f'{func.__name__}.json', 'a', encoding='utf-8') as file:
            json.dump(res_and_param, file, ensure_ascii=False)
        return res

    return wrapper


@save_as_json
def triangle_valid(a, v, d, *, side_one: int, side_two: int, side_three: int):
    if side_one < side_two + side_three and side_two < side_one + side_three and side_three < side_two + side_one:
        if side_one == side_two == side_three:
            print('Валидный равносторонний')
        elif side_one == side_two or side_two == side_three or side_three == side_one:
            print('Валидный равнобедренный')
        else:
            print('Валидный разносторонний')
    else:
        print('Треугольник не существует')
    return side_two + side_three + side_one


# Зад 4 + 6
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
def echo(count: int):
    def dec(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = None
            for i in range(count):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return dec


@echo(5)
def hello():
    print('Hello world')


# Зад 5 + 6
@check
@echo(2)
@save_as_json
def guess_n(number: int, count: int):
    counter = count
    while counter > 0:
        n = int(input('Введите число: '))
        counter -= 1
        if n < number:
            print(f'Больше ост{counter}')
        if n > number:
            print(f'Меньше ост{counter}')
        if n == number:
            print('Победа')
            return 'Победа'
        if counter == 0:
            print('Конец')
            return 'Конец'


# Дз
# Напишите следующие функции:
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
def create_csv_equation():
    count = ri(100, 1000)
    list_const = [[ri(1, 9), ri(0, 9), ri(0, 9)] for i in range(count)]
    file = 'quadratic_equation.csv'
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list_const)
    return file


def find_roots_equations_csv(func: Callable):
    def deco(func2: Callable):
        def wrapper(*args, **kwargs):
            path = func()
            roots = {}
            with open(path, 'r') as f:
                line = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
                for l_ in line:
                    args = l_
                    res = func2(*args, **kwargs)
                    roots[str(l_)] = str(res)
            return roots

        return wrapper

    return deco


def save_as_json(func: Callable):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('result.json', 'w') as f:
            json.dump(res, f)

    return wrapper


@save_as_json
@find_roots_equations_csv(create_csv_equation)
def roots_quadratic_equation(number_a: int, number_b: int, number_c: int):
    disc = number_b ** 2 - 4 * number_a * number_c
    if disc >= 0:
        x1, x2 = (-1 * number_b + math.sqrt(disc)) / (2 * number_a), (-1 * number_b - math.sqrt(disc)) / (2 * number_a)
        x1, x2 = round(x1, 3), round(x2, 3)
    else:
        x1, x2 = complex(round((-1 * number_b) / (2 * number_a), 3),
                         round(math.sqrt(disc * -1) / (2 * number_a), 3)), complex(
            round((-1 * number_b) / (2 * number_a), 3), round(-1 * math.sqrt(disc * -1) / (2 * number_a), 3))
    return x1, x2


if __name__ == '__main__':
    # guess_number(10, 4)
    # guess(102, 4)
    # triangle_valid(2, 4, 6, side_one=5, side_two=7, side_three=4)
    # hello()
    # guess_n(107, 4)
    # create_csv_equation()
    r = roots_quadratic_equation(1, 1, 1)
    print(r)
