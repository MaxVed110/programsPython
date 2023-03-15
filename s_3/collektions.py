import operator
import string
from itertools import combinations


# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
def search_duplicates(primary_list: list):
    res_list = []
    while primary_list:
        buf = primary_list.pop()
        if buf in primary_list:
            res_list.append(buf)
    return res_list


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
def frequent_words(text_: str):
    dict_word = {}
    text_ = text_.translate(str.maketrans('', '', string.punctuation))
    text_ = text_.lower()
    buf = text_.split(' ')
    for word in buf:
        if word not in dict_word.keys():
            dict_word[word] = buf.count(word)
    dict_word = sorted(dict_word.items(), key=operator.itemgetter(1), reverse=True)
    if len(dict_word) < 10:
        res = [dict_word[i][0] for i in range(len(dict_word))]
    else:
        res = [dict_word[i][0] for i in range(10)]
    return res


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
def shove_things(dict_things: dict, load_capacity: int):
    res_list = []
    for i in range(1, len(dict_things)):
        for x in combinations(dict_things, i):
            sum_mass = 0
            buf_dic = {z: dict_things[z] for z in x}
            for val in buf_dic.values():
                sum_mass += val
            if sum_mass <= load_capacity:
                res_list.append(buf_dic)
    for i in res_list:
        print(i)


if __name__ == '__main__':
    # w = [1, 3, 5, 7, 5, 3, 1]
    # print(search_duplicates(w))
    # text = 'Временная сложность сортировки словаря с использованием функции itemgetter() равна O(n log n).' \
    #        'Это связано с тем, что функция itemgetter() должна проходить через словарь и сравнивать каждый элемент,' \
    #        'чтобы определить порядок сортировки. Поскольку сравнение каждого элемента - это операция O (n), а' \
    #        'сортировка - операция O (log n), общая временная сложность составляет O (n log n).'
    # print(frequent_words(text))
    test = {'1': 3, '2': 5, '3': 2, '4': 7}
    shove_things(test, 10)
