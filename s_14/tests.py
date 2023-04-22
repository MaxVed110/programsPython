def triangle_valid(side_one: int, side_two: int, side_three: int):
    """
    Checks the existence of a triangle.
    >>> triangle_valid(5,5,5)
    'Валидный равносторонний'
    >>> triangle_valid(5,5,8)
    'Валидный равнобедренный'
    >>> triangle_valid(5,4,8)
    'Валидный разносторонний'
    >>> triangle_valid(5,4,80)
    'Треугольник не существует'
    """
    if side_one < side_two + side_three and side_two < side_one + side_three and side_three < side_two + side_one:
        if side_one == side_two == side_three:
            return 'Валидный равносторонний'
        elif side_one == side_two or side_two == side_three or side_three == side_one:
            return 'Валидный равнобедренный'
        else:
            return 'Валидный разносторонний'
    else:
        return 'Треугольник не существует'


def simple_or_compound(number):
    """
    Checks the number for simplicity
    >>> simple_or_compound(11)
    'Число является простым'
    >>> simple_or_compound(2)
   ' Простое число'
    >>> simple_or_compound(1)
    'Число не является ни простым, ни составным'
    >>> simple_or_compound(4)
    'Число является составным'
    >>> simple_or_compound(35)
    'Число является составным'
    >>> simple_or_compound(1000000)
    'Число за рамками диапазона'
    """
    # number = int(input('Введите число: '))
    limitation = [0, 100000]
    if limitation[0] < number < limitation[1]:
        if number == 1:
            return 'Число не является ни простым, ни составным'

        elif number <= 3:
            return 'Простое число'

        elif number % 2 == 0 or number % 3 == 0:
            return 'Число является составным'

        i = 5
        while i ** 2 <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return 'Число является составным'
            i += 6
        return 'Число является простым'
    else:
        return 'Число за рамками диапазона'


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
