def update_grid(column, row_, symbol):
    next_sign_ = symbol
    if grid[column - 1][row_ - 1] == "-":
        grid[column - 1][row_ - 1] = symbol
        new_grid(grid)
        return next_sign_
    else:
        return input('Место занято, сходите иначе: '), update_grid(column, row_, symbol)


def new_grid(a):
    print(*a, sep='\n')


#  def winner_is():


n = 3
grid = [["-" for c in range(n)] for r in range(n)]
sign = ["-", "X", "O"]
next_sign = sign[1]
move = input("Крестики ходят первые: ")
col, row = list(map(int, move.split(' ')))
grid[col - 1][row - 1] = next_sign
new_grid(grid)

counter = grid[row].count("-")
print(counter)
# condition = "-" in grid[row]
# print(condition)

while counter > 0:
    if next_sign == sign[1]:
        next_sign = sign[2]
        move = input("Нолики ходят: ")
    else:
        next_sign = sign[1]
        move = input("Крестики ходят: ")
    col, row = list(map(int, move.split(' ')))
    update_grid(col, row, next_sign)
    counter -= 1
    print(counter)
else:
    print("Игра закончилась вничью")


