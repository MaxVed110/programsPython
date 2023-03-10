from fractions import Fraction
from sympy import divisors


# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def new_hex(number: int):
    buf_lst = []
    while number > 0:
        buf = number % 16
        match buf:
            case 10:
                buf = 'a'
            case 11:
                buf = 'b'
            case 12:
                buf = 'c'
            case 13:
                buf = 'd'
            case 14:
                buf = 'e'
            case 15:
                buf = 'f'
            case _:
                buf = str(buf)
        buf_lst.append(buf)
        number //= 16
    buf_lst.reverse()
    print(''.join(buf_lst))


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа
# должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

def sum_and_product_of_fractions(fractions_one: str, fractions_two: str):

    def shorten_the_fraction(fraction: list):
        div = 0
        for i in divisors(fraction[0]):
            if i in divisors(fraction[1]):
                div = i
        fraction[0] //= div
        fraction[1] //= div
        return fraction

    fr_one_lst, fr_two_lst = list(map(int, fractions_one.split('/'))), list(map(int, fractions_two.split('/')))

    # первичное сокращение дробей
    fr_one_lst = shorten_the_fraction(fr_one_lst)
    fr_two_lst = shorten_the_fraction(fr_two_lst)

    # основные операции
    if fr_one_lst[1] == fr_two_lst[1]:
        sum_ = [fr_one_lst[0] + fr_two_lst[0], fr_one_lst[1]]
    else:
        buf1 = fr_one_lst[0] * fr_two_lst[1]
        buf2 = fr_two_lst[0] * fr_one_lst[1]
        sum_ = [buf1 + buf2, fr_one_lst[1] * fr_two_lst[1]]
    mult = [fr_one_lst[0] * fr_two_lst[0], fr_one_lst[1] * fr_two_lst[1]]

    # вторичное сокращение дробей
    sum_ = shorten_the_fraction(sum_)
    mult = shorten_the_fraction(mult)

    # вывод
    sum_ = list(map(str, sum_))
    mult = list(map(str, mult))
    sum_ = '/'.join(sum_)
    mult = '/'.join(mult)
    return sum_, mult


if __name__ == '__main__':
    print(sum_and_product_of_fractions('1/4', '1/4'))
    print(Fraction(2, 4) + Fraction(2, 6))
    print(Fraction(2, 4) * Fraction(2, 6))

