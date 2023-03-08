from random import randint


# 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle_valid(side_one: int, side_two: int, side_three: int):
    if side_one < side_two + side_three and side_two < side_one + side_three and side_three < side_two + side_one:
        if side_one == side_two == side_three:
            print('Валидный равносторонний')
        elif side_one == side_two or side_two == side_three or side_three == side_one:
            print('Валидный равнобедренный')
        else:
            print('Валидный разносторонний')
    else:
        print('Треугольник не существует')


# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def simple_or_compound():
    number = int(input('Введите число: '))
    limitation = [0, 100000]
    if limitation[0] < number < limitation[1]:
        if number == 1:
            print('Число не является ни простым, ни составным')
            return
        elif number <= 3:
            print('Простое число')
            return
        elif number % 2 == 0 or number % 3 == 0:
            print('Число является составным')
            return
        i = 5
        while i ** 2 <= number:
            if number % i == 0 or number % (i + 2) == 0:
                print('Число является составным')
                return
            i += 6
        print('Число является простым')
    else:
        return 'Число за рамками диапазона'


# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
# подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

def guess_the_number():
    number = randint(0, 1000)
    flag = False
    for i in range(1, 11):
        print(f'Попытка {i}, осталось: {11 - i}')
        num_us = int(input(f'Введите число: '))
        if num_us > number:
            print('Загаданное число меньше\n')
        if num_us < number:
            print('Загаданное число больше\n')
        if num_us == number:
            print('Вы выиграли, игра завершена')
            flag = True
            break
    if not flag:
        print(f'Вы проиграли, игра завершена\nОтвет {number}')


if __name__ == '__main__':
    # triangle_valid(10, 20, 10)
    # simple_or_compound()
    guess_the_number()
