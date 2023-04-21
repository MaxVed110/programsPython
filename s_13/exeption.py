import json


# Зад 1
def func_inp():
    print('Введите число... ')
    while True:
        try:
            a = float(input())
            break
        except ValueError:
            print('Введите число')


# Зад 2
def dict_get(in_dict: dict, key, val_def):
    try:
        return in_dict[key]
    except KeyError:
        return val_def


# Зад 4
class UserPass:
    _id_gl = []
    _dict_us = {}
    NAME_FILE_OUT = 'save_data_us.json'

    def __init__(self, name='root', val_id=0, val_level=0):
        self.name = name
        self._id = self.id(val_id)
        self._level = val_level
        self.add_in_dict()

    def __eq__(self, other):
        first = self.name == other.name
        second = self.id == other.id
        return first == second

    @property
    def id(self):
        return self._id

    @property
    def level(self):
        return self._level

    @id.setter
    def id(self, val):
        try:
            id_us = int(val)
            if val != 0 and self._level != 0:
                if id_us not in self._id_gl:
                    self._id_gl.append(id_us)
                    self._id = id_us
                else:
                    print('Повторите')
            if val == 0 and self._level == 0:
                self._id = 0
        except ValueError as e:
            print(f'Повторите, {e}')

    @level.setter
    def level(self, val):
        if val != 0:
            if val > self._level:
                raise Exception('Отказано в доступе')
            else:
                self._level = val

    def add_in_dict(self):
        def save_json(file: str, datas: dict):
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(datas, f)

        if self._level not in self._dict_us.keys():
            self._dict_us[self._level] = [[self.name, self._id]]
            save_json(self.NAME_FILE_OUT, self._dict_us)
        else:
            self._dict_us[self._level].append([[self.name, self._id]])
            save_json(self.NAME_FILE_OUT, self._dict_us)


def load_data_us_from_json(file):
    set_user = set()
    with open(file, 'r') as f:
        dict_j = json.load(f)

    for key in dict_j.keys():
        a = UserPass(dict_j[key][0], dict_j[key][1], key)
        set_user.add(a)


# Зад 3, 6
class UserExept(Exception):
    pass


class LevelError(UserExept):
    def __str__(self):
        return 'Уровень добавляемого пользователя не может превышать Ваш уровень'


class AccessError(UserExept):
    def __init__(self, val: UserPass, string=''):
        self.val = val
        self.str = string

    def __str__(self):
        if self.str != '':
            return self.str
        else:
            return f'Такого пользователя ({self.val.name}, {self.val.id}) в системе не зарегистрировано'


# Зад 5
class Authorization:
    NAME_FILE_IN = 'load_data_us.json'

    def __init__(self):
        self._dict_us = {}
        self._set_user = set()

    def _add_in_dict(self):
        for i in self._set_user:
            if i.level not in self._dict_us.keys():
                self._dict_us[i.level] = [[i.name, i.id]]
            else:
                self._dict_us[i.level].append([[i.name, i.id]])

    def load_data_us_from_json(self, file=NAME_FILE_IN):
        with open(file, 'r') as f:
            dict_j = json.load(f)

        for key in dict_j.keys():
            buf = UserPass(dict_j[key][0], dict_j[key][1], key)
            self._set_user.add(buf)
        self._add_in_dict()

    def log_in_system(self):
        try:
            a = input('Введите имя: ')
            b = int(input('Введите id: '))
            us = UserPass(a, b)
            for i in self._set_user:
                if i == us:
                    return i.level
                else:
                    raise AccessError(us)
        except ValueError:
            print('Попробуйте снова')

    def add_user(self):
        level = self.log_in_system()

        try:
            a = input('Введите имя пользователя, которого нужно добавить: ')
            b = int(input('Введите его id: '))
            l = int(input('Введите уровень доступа пользователя: '))
            if l > level:
                raise LevelError
            us = UserPass(a, b)
            for i in self._set_user:
                if i == us:
                    raise AccessError(us, 'Такой пользователь уже существует')
                else:
                    raise AccessError(us)
        except ValueError:
            print('Попробуйте снова')


# ДЗ
class RectangleExept(Exception):
    pass


class DifferenceExept(RectangleExept):
    def __init__(self, value):
        self.val = value

    def __str__(self):
        return f'Нельзя создасть фигуру со стороной отрицательной длины: {self.val}'


class NegativeSideExept(RectangleExept):
    def __init__(self, perimeter_one, perimeter_two):
        self.one = perimeter_one
        self.two = perimeter_two

    def __str__(self):
        return f'При вычислении разности фигур произошла ошибка. Вторая фигура {self.two} больше первой {self.one}, ' \
               f'а это не допустимо'


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
            raise DifferenceExept(value)

    @b.setter
    def b(self, value):
        if value >= 0:
            self._b = value
        else:
            raise DifferenceExept(value)

    def __add__(self, other):
        new_per = self.perimeter() + other.perimeter()
        return Rectangle(new_per / 2)

    def __sub__(self, other):
        new_per = self.perimeter() - other.perimeter() if self.perimeter() > other.perimeter() else -1
        if new_per == -1:
            raise NegativeSideExept(self.perimeter(), other.perimeter())
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


if __name__ == '__main__':
    f = 1
    s = 7
    a = f == s
    print(a)
