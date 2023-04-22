import unittest

from tests import triangle_valid, simple_or_compound


class TestFunc(unittest.TestCase):

    def test_verification_of_claims_triangle(self):
        self.assertEqual(triangle_valid(5, 5, 5), 'Валидный равносторонний')
        self.assertEqual(triangle_valid(5, 5, 8), 'Валидный равнобедренный')
        self.assertEqual(triangle_valid(5, 4, 8), 'Валидный разносторонний')
        self.assertEqual(triangle_valid(5, 5, 80), 'Треугольник не существует')

    def test_verification_of_claims_simple(self):
        self.assertEqual(simple_or_compound(11), 'Число является простым')
        self.assertEqual(simple_or_compound(2), 'Простое число')
        self.assertEqual(simple_or_compound(1), 'Число не является ни простым, ни составным')
        self.assertEqual(simple_or_compound(4), 'Число является составным')
        self.assertEqual(simple_or_compound(35), 'Число является составным')
        self.assertEqual(simple_or_compound(1000000), 'Число за рамками диапазона')


if __name__ == '__main__':
    unittest.main()
