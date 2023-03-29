import random
import os

__all__ = ['fill_the_file', 'pseudonyms', 'multiply_name', 'bite_file_gen', 'rename_files']


# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# количество строк и имя файла передаются как аргументы функции
def fill_the_file(count_lines: int, name_file: str):
    with open(name_file, 'a') as file:
        for i in range(count_lines):
            file.write(f'{random.randint(-1000, 1000)} | {random.triangular(-1000, 1000)}\n')


# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
def generator(size: int):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y',
                  'z']
    name = []
    flag = False
    for i in range(size):
        if random.randint(0, 1):
            name.append(vowels[random.randint(0, 4)])
            flag = True
        else:
            name.append(consonants[random.randint(0, 19)])
    if not flag:
        name.append(vowels[random.randint(0, 4)])
    name = ''.join(name)
    return name.title()


def pseudonyms(count_names: int, name_file: str):
    with open(name_file, 'a') as file:
        for i in range(count_names):
            file.write(f'{generator(random.randint(2, 8))}\n')


# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
def multiply_name(names_file: str, numbers_file: str, result_file: str):
    name_list = []
    num_mult_list = []
    res_list = []
    with open(names_file, 'r') as file_names:
        for line in file_names:
            name_list.append(line[:-1])

    with open(numbers_file, 'r') as file_numbers:
        for line in file_numbers:
            buf = line.split(' | ')
            num_mult_list.append(int(buf[0]) * float(buf[1][:-1]))
    nam = len(name_list)
    num = len(num_mult_list)
    for i in range(max(nam, num)):
        res_list.append([name_list[i % nam], num_mult_list[i % num]])
    with open(result_file, 'a') as file:
        for i in res_list:
            file.write(f'{i[0].upper() if i[1] >= 0 else i[0].lower()} | {i[1]}\n')


# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона
def bite_file_gen(extension: str, min_len_name=6, max_len_name=30, min_numb_bytes=265, max_numb_bytes=4096,
                  number_files=42):
    for i in range(number_files):
        name_file = f'{generator(random.randint(min_len_name, max_len_name)).lower()}.{extension}'
        with open(name_file, 'ba') as file:
            file.write(bytes(random.randint(min_numb_bytes, max_numb_bytes)))


#  Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
def rename_files(path: str, end_name: str, count_number: int, safe_name: list, orig_ext='txt', end_ext='docx'):
    dir_list = os.listdir(path)
    count_file = '0' * count_number
    count = 0
    for obj in dir_list:
        buf = obj.split('.')
        if buf[1] == orig_ext:
            try:
                buf[0] = f'{buf[0][safe_name[0]:(safe_name[1] + 1)]}{end_name}{count_file[:- (count // 10 + 1)]}{count}'
            except IndexError:
                buf[0] = f'{buf[0]}{end_name}{count_file[:- (count // 10 + 1)]}{count}'
            buf[1] = end_ext
            count += 1
            new = '.'.join(buf)
            os.rename(obj, new)


if __name__ == '__main__':
    # fill_the_file(6, 'test1.txt')
    # pseudonyms(5, 'test2.txt')
    # multiply_name('test2.txt', 'test1.txt', 'res.txt')
    rename_files('C:\\Users\\Максим\\Desktop\\Обучение\\Программы\\Погружение в python\\programs\\s_7', 'qqq', 2,
                 [1, 2])
