__all__ = ['rec_find']


def rec_find(columns, rows, solution):
    if len(solution) == rows:
        buf = []
        for i in range(len(solution)):
            buf.append([i, solution[i]])
        print(buf)

    for next_row in range(rows):
        if possibility_placement(columns, next_row, solution):
            rec_find(columns + 1, rows, solution + [next_row])


def possibility_placement(column, row, solution):
    for col in range(len(solution)):
        if solution[col] == row or abs(solution[col] - row) == abs(col - column):
            return False
    return True


def main():
    for i in range(8):
        rec_find(1, 8, [i])


if __name__ == '__main__':
    main()
