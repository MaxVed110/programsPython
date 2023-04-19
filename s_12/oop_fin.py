import csv
import json
from enum import Enum


# Зад 1, 2
class Factorial:
    SAVE_FILE = 'fct.json'

    def __init__(self, size_list):
        self.size_list = size_list
        self.dict_hist = {}

    def __str__(self):
        return f'Факториал чисел: {self.dict_hist}'

    def __call__(self, value):
        fct = 1
        if value < 0:
            raise ArithmeticError('Факториала отрицательного числа не существует')
        if value > 0:
            for i in range(1, value + 1):
                fct *= i
        if len(self.dict_hist.keys()) < self.size_list:
            self.dict_hist[value] = fct
        else:
            self.dict_hist.pop(next(iter(self.dict_hist)))
            self.dict_hist[value] = fct

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.SAVE_FILE, 'a') as f:
            json.dump(self.dict_hist, f, ensure_ascii=False)


# Зад 3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.
class FactorialGen:
    def __init__(self, stop, start=1, step=1):
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop < 0:
            raise ArithmeticError('Факториала не существует')
        while self.start <= self.stop:
            fct = 1
            for i in range(1, self.start + 1):
                fct *= i
            self.start += self.step
            return fct
        raise StopIteration


# Задание 4, 5
class Rectangle:
    __slots__ = ('_a', '_b')

    def __init__(self, wight, length=0):
        self._a = self.a = wight
        self._b = self.b = length

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value >= 0:
            self._a = value
        else:
            raise ArithmeticError

    @b.setter
    def b(self, value):
        if value >= 0:
            self._b = value
        else:
            raise ArithmeticError

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
            return f'Квадрат со стороной {self._a}'
        return f'Прямоугольник со сторонами {self._a} и {self._b}'

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


# Зад 6
class Valid:
    def __init__(self):
        ...

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):
        if value < 0:
            raise ArithmeticError


class Rec:
    a = Valid()
    b = Valid()

    def __init__(self, wight, length=0):
        self.a = wight
        self.b = length

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
class Valid_name:
    def __init__(self, min_range=0, max_range=0):
        self.min = min_range
        self.max = max_range

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, string):
        self.validate(string)
        setattr(instance, self.name, string)

    def validate(self, string):
        try:
            string.isalpha()
            if string.istitle():
                for ch in string:
                    if not ch.isalpha():
                        raise ValueError
        except AttributeError:
            if string < self.min or string > self.max:
                raise ValueError


class DiscType(Enum):
    MATHEMATICS = 'Mathematics'
    PHYSICS = 'Physics'
    HISTORY = 'History'
    LITERATURE = 'Literature'


class Student:
    last_name = Valid_name()
    first_name = Valid_name()
    point = Valid_name(0, 100)
    assessment = Valid_name(2, 5)
    PATH_FILE_DISC = ''

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        # self.discipline_dict = self.load_disc(self.PATH_FILE_DISC)
        self.discipline_dict = {'Mathematics': {'Тесты': [],
                                                'Оценки': []},
                                'Physics': {'Тесты': [],
                                            'Оценки': []},
                                'History': {'Тесты': [],
                                            'Оценки': []},
                                'Literature': {'Тесты': [],
                                               'Оценки': []}}

    def load_disc(self, file):
        dict_d = {}
        with open(file, 'r', newline='') as f:
            csv_f = csv.reader(f)
            for line in csv_f:
                dict_d[line] = {'Тесты': [],
                                'Оценки': []}
        return dict_d

    def set_test_res(self, disc: DiscType, assessment: int):
        self.point = assessment
        self.discipline_dict[disc.value]['Тесты'].append(self.point)

    def set_assessment_res(self, dics: DiscType, assessment: int):
        self.assessment = assessment
        self.discipline_dict[dics.value]['Оценки'].append(self.assessment)

    def average_score_test(self, disc: DiscType):
        try:
            return sum(self.discipline_dict[disc.value]['Тесты']) / len(self.discipline_dict[disc.value]['Тесты'])
        except ArithmeticError:
            return 'Что-то не так со списком оценок'

    def average_score_all_assessment(self):
        try:
            s = 0
            count = 0
            for key in self.discipline_dict.keys():
                if len(self.discipline_dict[key]['Оценки']) != 0:
                    s += sum(self.discipline_dict[key]['Оценки'])
                    count += len(self.discipline_dict[key]['Оценки'])
            return s / count
        except ArithmeticError:
            return 'Что-то пошло не так'


if __name__ == '__main__':
    a = Student('Aaaa', 'Msss')
    a.set_test_res(DiscType.HISTORY, 45)
    a.set_test_res(DiscType.HISTORY, 100)
    a.set_assessment_res(DiscType.HISTORY, 2)
    a.set_assessment_res(DiscType.MATHEMATICS, 5)
    a.set_assessment_res(DiscType.MATHEMATICS, 4)
    print(a.average_score_all_assessment())
