# 1.  Напишите функцию для транспонирования матрицы
def transposing_matrix(matrix_: list):
    tr_matrix = [[] for i in range(len(matrix_[0]))]
    for i in range(len(matrix_)):
        for item in range(len(matrix_[i])):
            tr_matrix[item].append(matrix_[i][item])
    print(tr_matrix)


# 2. Напишите функцию, принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление
def key_arguments(**kwargs):
    res_db = {}
    for key, value in kwargs.items():
        res_db[value] = key
    return res_db

# 3.  Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
class CashMachine:
    def __init__(self):
        self._history = []
        self._balance = 0
        self._cash_flag = False

    def replenish_balance(self, summ_replenish: int):
        if self._check_wealth():
            self._balance *= 0.9
        self._check_summ(summ_replenish)
        if self._cash_flag:
            self._balance += summ_replenish
        self._history.append('r')
        if self._check_history():
            self._balance *= 1.03
        print(f'Текущий баланс {self._balance}')

    def withdraw_money(self, summ_withdraw: int):
        if self._check_wealth():
            self._balance *= 0.9
        proc = summ_withdraw * 0.985
        if proc > self._balance - summ_withdraw:
            print('Недостаточно средств')
            print(f'Текущий баланс {self._balance}')
            return None
        self._check_summ(summ_withdraw, status='w')
        if self._cash_flag:
            self._balance -= summ_withdraw
            if 30 < proc < 600 and self._balance >= proc:
                self._balance -= summ_withdraw * 0.985
            if 30 <= self._balance < proc:
                self._balance -= 30
            if 600 < proc <= self._balance:
                self._balance -= 600
        self._history.append('w')
        if self._check_history():
            self._balance *= 1.03
        print(f'Текущий баланс {self._balance}')

    def _check_summ(self, summ, status='r'):
        if status == 'r':
            if summ <= 0 or summ % 50 != 0:
                print('Введите корректную сумму')
            else:
                self._cash_flag = True
        if status == 'w':
            if summ <= 0 or summ % 50 != 0 or summ > self._balance:
                print('Введите корректную сумму')
            else:
                self._cash_flag = True

    def _check_wealth(self):
        if self._balance >= 5000000:
            return True
        else:
            return False

    def _check_history(self):
        if len(self._history) % 3 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # matrix = [[1, 2, 0], [3, 4, 0], [5, 6, 0]]
    # transposing_matrix(matrix)
    # bal = CashMachine()
    # bal.replenish_balance(1000)
    print(key_arguments(one=1, three='три', two=2, four='четыре'))
