import os
import json
import csv
import pickle


# Зад 1
def txt_in_json(file: str):
    dict_n = {}
    with open(file, 'r') as f:
        for line in f:
            tmp = line.split(' | ')
            tmp[0].title()
            dict_n[tmp[0]] = float(tmp[1][:-1])
    with open('one_json.json', 'w') as f:
        json.dump(dict_n, f)


# Зад 2
def data_user(safe_file: str):
    data = {}
    base_id = []

    def save_json(file: str, datas: dict):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(datas, f)

    while True:
        name = input('Введите имя: ')
        id_ = input('Введите id: ')
        level = input('Введите уровень доступа: ')
        if id_ not in base_id:
            if level not in data.keys():
                data[level] = [[name, id_]]
                save_json(safe_file, data)
            else:
                data[level].append([name, id_])
                save_json(safe_file, data)
        else:
            print('Повторите')


# Зад 3
def json_to_csv(file: str):
    buf = []
    with open(file, 'r') as f:
        dict_j = json.load(f)
    for keys in dict_j.keys():
        for item in dict_j[keys]:
            tmp = [keys]
            tmp.extend(item)
            buf.append(tmp)
    with open('data_csv.csv', 'w', encoding='utf-8'):
        writer_csv = csv.writer(f)
        writer_csv.writerow(['Уровень доступа', 'Id', 'Имя'])
        writer_csv.writerows(buf)


# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
def info_directory(path: str):
    def get_data(path_: str):
        result_directory = {}
        for i, j, k in os.walk(path_):
            for folder in j:
                size = 0
                for i_, j_, k_ in os.walk(f'{i}/{folder}'):
                    for file in k_:
                        size += os.path.getsize(f'{i_}/{file}')
                result_directory[folder] = {'type': 'is directory',
                                            'parent': i.split('\\')[-1],
                                            'size': size}
            for file in k:
                result_directory[file] = {'type': 'is file',
                                          'parent': i.split('\\')[-1],
                                          'size': os.path.getsize(f"{i}/{file}")}
        return result_directory

    data = get_data(path)

    with open('info_dir_js.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    with open('info_dir_cs.csv', 'w', encoding='utf-8') as f:
        writer_csv = csv.writer(f)
        writer_csv.writerow(['file', 'type', 'parent', 'size'])
        buf = []
        for key in data.keys():
            temp = [key]
            for value in data[key].values():
                temp.append(value)
            buf.append(temp)
        writer_csv.writerows(buf)
    with open('info_dir_picle.picle', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    # pathk = 'C:\\Users\\Максим\\Desktop\\Обучение\\Программы\\Погружение в python\\programs'
    # info_directory(pathk)
    # txt_in_json('res.txt')
    data_user('sss.json')
