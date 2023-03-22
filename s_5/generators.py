# # 1
# def dict_numbers(numbers: str):
#     val1, key1, key2, *val2 = numbers.split('/')
#     return {key1: val1, key2: tuple(val2)}
#
#
# # 2
# def dict_chr(string: str):
#     return {ch: ord(ch) for ch in string}
#
#
# # 4
# def generator_even_numbers(lim: int):
#     return (i for i in range(lim + 1) if i % 2 == 0 and i % 10 + i // 10 % 10 != 8)
#
#
# # 5
# def fizz_buzz(lim: int):
#     return ('fizzBizz' if i % 15 == 0 else 'fizz' if i % 3 == 0 else 'bizz' if i % 5 == 0 else i for i in
#             range(lim + 1))
#
#
# # 6
# def multiplication_table():
#     return (f'{i} x {j} = {i * j}' for i in range(11) for j in range(11))


# 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def path_and_name_file(path_: str):
    *_, name = path_.split('/')
    extension = name.split('.')[1]
    return path_, name, extension


# 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой
# длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате
# получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии
def dict_generator(names: list, salarys: list, prizes: list):
    if len(names) == len(salarys) == len(prizes):
        try:
            return {names[i]: salarys[i] * float(prizes[i][:-1]) / 100 + salarys[i] for i in range(len(names))}
        except TypeError:
            print('Число введено в неправильном формате')
            return None
    print('Длины списков не равны')
    return None


# 3. Создайте функцию генератор чисел Фибоначчи
def fibo_gen(number: int):
    num_fib = 1
    pre_num_fib = 1
    pre_pre_num_fib = 0
    for i in range(1, number + 1):
        if i == 1:
            yield num_fib
        num_fib = pre_num_fib + pre_pre_num_fib
        pre_pre_num_fib = pre_num_fib
        pre_num_fib = num_fib
        yield num_fib


if __name__ == '__main__':
    path = 'C:/Users/Максим/Desktop/Обучение/Программы/Погружение в python/programs/s_5/generators.py'
    print(path_and_name_file(path))
    srt = '10%'
    print(int(srt[:-1]))
    name_ = ['a', 'b', 'c']
    salary = [100, 200, 300]
    prize = ['10.25', '20%', '20%']
    a = 10.25
    print(dict_generator(name_, salary, prize))

