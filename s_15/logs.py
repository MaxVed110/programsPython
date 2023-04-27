import argparse
import random
import logging
from typing import Callable
from datetime import date, timedelta

FORMAT = '%(asctime)s %(name)s - %(lineno)s line(s) - %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, filename='logs.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Зад 1
def dif_zero(a, b):
    try:
        return a / b
    except ArithmeticError as e:
        logger.error(f'{dif_zero.__name__} - {e}')


# Зад 2, 3
def logg_info(flag=True, msg=''):
    def dec(func: Callable):
        def wrapper(*args, **kwargs):
            if flag:
                logger.warning(f'{func.__name__} - {msg} - {func(*args, **kwargs)}')
            else:
                logger.debug(f'{func.__name__} - {msg} - {func(*args, **kwargs)}')

        return wrapper

    return dec


@logg_info(flag=False)
def dif_zero_new(a, b):
    try:
        return a / b
    except ArithmeticError as e:
        return f'{a}, {b}, {e}'


# Зад 4
def calendar(date_in: str):
    date_pars = date_in.split(' ')
    date_pars[0] = int(date_pars[0][0:1])
    date_pars[2] = date_pars[2][0:3]
    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    mou = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    for i in range(len(week)):
        if date_pars[1] == week[i]:
            date_pars[1] = i
    if type(date_pars[1]) == str:
        logger.error('Формат недели неверный')
        raise ValueError('Формат недели неверный')
    for i in range(len(mou)):
        if date_pars[2] == mou[i]:
            date_pars[2] = i
    if type(date_pars[2]) == str:
        logger.error('Формат месяца неверный')
        raise ValueError('Формат месяца неверный')
    d = date(year=2023, month=date_pars[2], day=1)
    td = timedelta(weeks=date_pars[1] - 1, days=date_pars[0])
    try:
        return d + td
    except Exception as e:
        logger.error(f'Неверный формат, {e}')


# ДЗ
def generator():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('size', metavar='N', type=int, default=1)
        ars = parser.parse_args()
    except Exception as e:
        logger.error(f'{generator.__name__} --> {e}')

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y',
                  'z']
    name = []
    flag = False
    for i in range(ars.size[0]):
        if random.randint(0, 1):
            name.append(vowels[random.randint(0, 4)])
            flag = True
        else:
            name.append(consonants[random.randint(0, 19)])
    if not flag:
        name.append(vowels[random.randint(0, 4)])
    name = ''.join(name)
    logger.info(f'{generator.__name__} --> сгенерировано имя {name}')
    return name.title()


if __name__ == '__main__':
    calendar('1-й четверг ноября')
