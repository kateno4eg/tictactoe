def update_grid(column, row_, symbol):
    grid[column - 1][row_ - 1] = symbol
    return new_grid(grid)


def new_grid(a):
    header = {k + 1: [el for el in l] for k, l in enumerate(a)}
    print("  " + ' '.join(map(str, header.keys())))
    for i, item in enumerate(a, 1):
        print(i, ' '.join(map(str, item)))


def winner_is(a):  # доработать
    for el in a:
        a_set = set(el)
        if len(a_set) == 1 and a_set != {'-'}:
            print(f'Победа {a_set}!')  # доработать вывод
            return True
        else:
            pass


n = 3
grid = [["-" for c in range(n)] for r in range(n)]
sign = ["X", "O"]
next_sign = sign[0]

move = input("Крестики ходят первые: ")
col, row = list(map(int, move.split(' ')))
grid[col - 1][row - 1] = next_sign
new_grid(grid)

condition_1 = any(['-' in row for row in grid])
while condition_1 and winner_is(grid) is not True:
    if next_sign == sign[0]:
        next_sign = sign[1]
        move = input("Нолики ходят: ")
    else:
        next_sign = sign[0]
        move = input("Крестики ходят: ")
    col, row = list(map(int, move.split(' ')))
    if 0 < col <= n and 0 < row <= n:
        if grid[col - 1][row - 1] == "-":
            update_grid(col, row, next_sign)
        else:
            move = input("Место занято, сходите иначе: ")
            col, row = list(map(int, move.split(' ')))
            update_grid(col, row, next_sign)
    else:
        move = input(f"Введите число в диапазоне от 0 до {n} включительно: ")
        col, row = list(map(int, move.split(' ')))
        update_grid(col, row, next_sign)
    condition = any(['-' in row for row in grid])
    winner_is(grid)
else:
    print("Игра окончена")  # добавить условие победы в игре


