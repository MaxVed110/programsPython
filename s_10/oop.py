import csv
import json
import math


# Зад 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        return self.radius * math.pi

    def circle_area(self):
        return self.radius ** 2 * math.pi


# Зад 2
class Rectangle:
    def __init__(self, a_length, b_width=0):
        self.a = a_length
        self.b = b_width

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


# Зад 3
class DataHuman:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    def birthday(self, delta: int, sign=True):
        if sign:
            self._age += delta
        else:
            if self._age < delta:
                raise ValueError('Возраст не может быть отрицательным')
            else:
                self._age -= delta

    def get_info(self):
        return f'{self.first_name} {self.last_name}, возраст - {self._age}'


# Зад 4
class Staff(DataHuman):
    def __init__(self, first_name, last_name, age, id_: int):
        super().__init__(first_name, last_name, age)
        self.id = self._assign_id(id_)
        self.access_level = self._calculate_access_level(self.id)

    def _assign_id(self, id_: int):
        if len(str(id_)):
            raise ValueError('Неверный id')
        else:
            return id_

    def _calculate_access_level(self, id_):
        sum_ = 0
        while id_ > 0:
            sum_ += id_ % 10
            id_ /= 10
        return sum_ % 7


# Зад 5, 6
class Animal:
    def __init__(self, name: str, age: int, masse: int):
        self.name = name
        self.age = age
        self.masse = masse

    def get_general_info(self):
        return f'{self.age}, {self.age}, {self.masse}'


class Cat(Animal):
    def __init__(self, name: str, age: int, masse: int):
        super().__init__(name, age, masse)
        self.noise = 'Мяу'

    def specific_info(self):
        return f'Звуки: {self.noise}'


class Dog(Animal):
    def __init__(self, name: str, age: int, masse: int):
        super().__init__(name, age, masse)
        self.noise = 'Гав'
        self.list_commands = []

    def specific_info(self):
        return f'Звуки: {self.noise}, команды: {self.list_commands}'


class Hamster(Animal):
    def __init__(self, name: str, age: int, masse: int):
        super().__init__(name, age, masse)
        self.noise = 'Звуки хомяка'

    def specific_info(self):
        return f'Звуки: {self.noise}'


# ДЗ
class FactoryAnimals:

    def creator(self, type_a, name, age, masse):
        if type_a == 'Кот':
            return Cat(name, age, masse)
        if type_a == 'Пес':
            return Dog(name, age, masse)
        if type_a == 'Хомяк':
            return Hamster(name, age, masse)


class WorkingWithFiles:
    def __init__(self, name_file: str, name_new=None):
        self.file_name = name_file
        self.new_file = name_new

    def txt_in_json(self, name_txt, name_json=None):
        dict_n = {}
        with open(name_txt, 'r') as f:
            for line in f:
                tmp = line.split(' | ')
                tmp[0].title()
                dict_n[tmp[0]] = float(tmp[1][:-1])
        if name_json is None:
            with open(f'{name_txt[:-4]}.json', 'w') as f:
                json.dump(dict_n, f)
        else:
            with open(f'{name_json}.json', 'w') as f:
                json.dump(dict_n, f)

    def json_to_csv(self, name_json, name_csv=None):
        buf = []
        with open(name_json, 'r') as f:
            dict_j = json.load(f)
        for keys in dict_j.keys():
            for item in dict_j[keys]:
                tmp = [keys]
                tmp.extend(item)
                buf.append(tmp)
        if name_csv is None:
            with open(f'{name_json[:-5]}.csv', 'w', encoding='utf-8'):
                writer_csv = csv.writer(f)
                writer_csv.writerow(['Уровень доступа', 'Id', 'Имя'])
                writer_csv.writerows(buf)
        else:
            with open(name_csv, 'w', encoding='utf-8'):
                writer_csv = csv.writer(f)
                writer_csv.writerow(['Уровень доступа', 'Id', 'Имя'])
                writer_csv.writerows(buf)


if __name__ == "__main__":
    a = DataHuman('aff', 'asaf', 23)
