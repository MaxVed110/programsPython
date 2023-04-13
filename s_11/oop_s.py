import getpass
import time
from operator import add


# Зад 1, 3
class MyStr(str):
    """ The class extends the functionality of the standard string data type """

    def __new__(cls, value):
        inst = super().__new__(cls, value)
        inst.author = getpass.getuser()
        inst.time_create = time.time()
        return inst

    def __str__(self):
        return f'{self.author}, {self.time_create}, {self = } '


# Зад 2, 3, 4
# Добавьте методы представления экземпляра для программиста
# и для пользователя.
class Archive:
    """ The class saves previously transmitted data in dictionary format """
    dic = dict()

    def __init__(self, number, st):
        self.number = number
        self.st = st
        self.dic[number] = st

    def __repr__(self):
        return f'Archive({self.number}, {self.st})'

    def __str__(self):
        return f'Содержит: {self.number}, {self.st}'


# Зад 5, 6
class Rectangle:
    def __init__(self, a_length, b_width=0):
        self.a = a_length
        self.b = b_width

    def __add__(self, other):
        new_per = self.perimeter() + other.perimeter()
        return Rectangle(new_per / 2)

    def __sub__(self, other):
        new_per = self.perimeter() - other.perimeter() if self.perimeter() > other.perimeter() else -1
        if new_per == -1:
            raise Exception('Отрицательный периметр')
        return Rectangle(new_per / 2)

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() >= other.area()

    def __str__(self):
        if self.b == 0:
            return f'Квадрат со стороной {self.a}'
        return f'Прямоугольник со сторонами {self.a} и {self.b}'

    def perimeter(self):
        if self.b == 0:
            return self.a * 4
        else:
            return 2 * (self.a + self.b)

    def area(self):
        if self.b == 0:
            return self.a ** 2
        else:
            return self.a * self.b


# ДЗ
class Matrix:
    def __init__(self, lines, columns, data: []):
        self.lines = lines
        self.columns = columns
        self.matrix = self.set_matrix(lines, columns, data)

    def __add__(self, other):
        res = []
        if self.lines == other.lines and self.columns == other.columns:
            for i in range(self.lines):
                for j in range(self.columns):
                    res.append(self.matrix[i][j] + other.matrix[i][j])
        return self.set_matrix(self.lines, self.columns, res)

    def __eq__(self, other):
        """Сравниваются значения"""
        return self.matrix == other.matrix

    def __gt__(self, other):
        """Сравнивается размер"""
        return self.lines * self.columns > other.lines * other.columns

    def __le__(self, other):
        """Сравнивается размер"""
        return self.lines * self.columns >= other.lines * other.columns

    def __mul__(self, other):
        res = [[0 for i in range(other.columns)] for i in range(self.lines)]
        if self.columns == other.lines:
            for i in range(self.lines):
                for j in range(other.columns):
                    for k in range(other.lines):
                        res[i][j] += self.matrix[i][k] * other.matrix[k][j]
        buf = []
        while res:
            buf.extend(res.pop(0))
        return Matrix(self.lines, other.columns, buf)

    def __str__(self):
        st = ''
        for i in range(self.lines):
            st += f'{self.matrix[i]}\n'
        return st

    def set_matrix(self, lines, columns, data: []):
        matrix = [[] for i in range(lines)]
        count = 0
        if len(data) != lines * columns:
            raise Exception('Объем данных не соответствует размеру')
        for i in range(lines):
            for j in range(columns):
                matrix[i].append(data[count])
                count += 1
        return matrix


if __name__ == '__main__':
    a = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
    b = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
    print(a)
    print(b)
    print(a * b)
