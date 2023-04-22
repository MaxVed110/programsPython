import pytest

from tests import triangle_valid, simple_or_compound


def test_verification_of_claims_triangle():
    assert triangle_valid(5, 5, 5) == 'Валидный равносторонний', 'Ошибка'
    assert triangle_valid(5, 5, 8) == 'Валидный равнобедренный', 'Ошибка'
    assert triangle_valid(5, 4, 8) == 'Валидный разносторонний', 'Ошибка'
    assert triangle_valid(5, 5, 50) == 'Треугольник не существует', 'Ошибка'


def test_verification_of_claims_simple():
    assert simple_or_compound(11) == 'Число является простым', 'Ошибка'
    assert simple_or_compound(2) == 'Простое число', 'Ошибка'
    assert simple_or_compound(1) == 'Число не является ни простым, ни составным', 'Ошибка'
    assert simple_or_compound(4) == 'Число является составным', 'Ошибка'
    assert simple_or_compound(35) == 'Число является составным', 'Ошибка'
    assert simple_or_compound(11000000) == 'Число за рамками диапазона', 'Ошибка'


if __name__ == '__main__':
    pytest.main()
