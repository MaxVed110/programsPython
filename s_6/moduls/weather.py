# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. Проверку года на високосность
# вынести в отдельную защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import re
import sys

__all__ = ['reality_date']


def reality_date(date: str):
    try:
        valid = re.match(r'\d{2}\.\d{2}\.\d{4}', date)
        valid = valid.group(0)
    except AttributeError:
        print("Введите корректный формат даты: DD.MM.YYYY")
        return False
    date = [int(a) for a in date.split('.')]
    if 1 <= date[1] <= 12 and 1 <= date[2] <= 9999:
        if _reality_day(date[0], date[1], date[2]):
            return True
    return False


def _reality_day(day: int, month: int, year: int):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= day <= 31:
            return True
    if month in [4, 6, 9, 11]:
        if 1 <= day <= 30:
            return True
    if month == 2:
        if _wis_year(year):
            if 1 <= day <= 29:
                return True
        if 1 <= day <= 28:
            return True
    return False


def _wis_year(year: int):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    if year % 4 == 0:
        return True
    return False


if __name__ == '__main__':
    name, dates, *param = sys.argv
    print(reality_date(dates))
