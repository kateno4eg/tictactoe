def update_grid(column, row_, symbol):
    grid[column - 1][row_ - 1] = symbol
    return new_grid(grid)


def new_grid(a):
    header = {k + 1: [el for el in l] for k, l in enumerate(a)}
    print("  " + ' '.join(map(str, header.keys())))
    for i, item in enumerate(a, 1):
        print(i, ' '.join(map(str, item)))


def winner_is(a):
    a_trans = [list(i) for i in zip(*a)]
    for r in a_trans:
        if all(el == "X" for el in r) or all(el == "O" for el in r):
            return True
    for r in a:
        if all(el == "X" for el in r) or all(el == "O" for el in r):
            return True
    for r in range(len(a)):
        if all(a[i][i] == "X" for i in range(len(a))) or all(a[i][i] == "O" for i in range(len(a))):
            return True
    for r in range(len(a)):
        if all(a[i][len(a) - 1 - i] == "X" for i in range(len(a))):
            return True
        elif all(a[i][len(a) - 1 - i] == "O" for i in range(len(a))):
            return True
    return False


n = 3
grid = [["-" for c in range(n)] for r in range(n)]
sign = ["X", "O"]
next_sign = sign[0]

move = input("Крестики ходят первые: ")
col, row = list(map(int, move.split(' ')))
grid[col - 1][row - 1] = next_sign
new_grid(grid)

condition = any(['-' in row for row in grid])
while winner_is(grid) is False:
    if condition:
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
        print(winner_is(grid))
    else:
        print("Игра окончена вничью")
        break
else:
    if next_sign == sign[0]:
        print(f"Крестики победили!")
    if next_sign == sign[1]:
        print(f"Нолики победили!")
