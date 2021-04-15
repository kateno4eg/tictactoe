def update_grid(column, row_, symbol):
    while grid[column - 1][row_ - 1] == "-":
        grid[column - 1][row_ - 1] = symbol
        return new_grid(grid)
    else:
        input("Место занято, сходите иначе: ")
#        return update_grid(column, row_, symbol)


def new_grid(a):
    header = {k + 1: [el for el in l] for k, l in enumerate(a)}
    print("  " + ' '.join(map(str, header.keys())))
    for i, item in enumerate(a, 1):
        print(i, ' '.join(map(str, item)))


def winner_is(a, r):  # доработать
    a_set = set(a[r])
    if len(a_set) == 1 and a_set != {'-'}:
        print(f'Победа {a_set}!')
    else:
        pass


n = 3
grid = [["-" for c in range(n)] for r in range(n)]
sign = ["X", "O"]
next_sign = sign[0]
move = input("Крестики ходят первые: ")  # включить в цикл?
col, row = list(map(int, move.split(' ')))
grid[col - 1][row - 1] = next_sign
new_grid(grid)

condition = any(['-' in row for row in grid])
while condition:
    if next_sign == sign[0]:
        next_sign = sign[1]
        move = input("Нолики ходят: ")
    else:
        next_sign = sign[0]
        move = input("Крестики ходят: ")
    col, row = list(map(int, move.split(' ')))
    update_grid(col, row, next_sign)
    condition = any(['-' in row for row in grid])
#    winner_is(grid, row)
else:
    print("Игра закончилась вничью")


