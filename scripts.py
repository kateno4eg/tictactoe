
n = 3
grid = [["-" for col in range(n)] for row in range(n)]
sign = ["-", "X", "O"]
next_sign = sign[1]
move = input("Крестики ходят первые: ")
col, row = list(map(int, move.split(' ')))
grid[col - 1][row - 1] = sign
print(*grid, sep='\n')


def update_grid(column, row_, symbol):
    next_sign_ = symbol
    if grid[column - 1][row_ - 1] == "-":
        grid[column - 1][row_ - 1] = symbol
        new_grid(grid)
        return next_sign_
    else:
        return input('Место занято, сходите иначе: ') + update_grid(column, row_, symbol)


def new_grid(a):
    print(*a, sep='\n')


if "-" in grid[row]:
    if sign == sign[1]:
        next_sign = sign[2]
        move = input("Нолики ходят: ")
        col, row = list(map(int, move.split(' ')))
        update_grid(col, row, sign)
    else:
        sign = sign[1]
        move = input("Крестики ходят: ")
        col, row = list(map(int, move.split(' ')))
        grid[col - 1][row - 1] = sign
        new_grid(grid)
else:
    print("Игра закончилась с каким-то результатом")

#  def winner_is():

#  for turn in range(1, turns + 1):
#     if turn == 1:
#         turn = input("Крестики ходят первые: ")  # формат хода "row-column", например 1 2, где 1 - строка, 2 -столбец
#         col, row = list(map(int, turn.split(' ')))
#         if grid[col - 1][row - 1] == "-":
#             grid[col - 1][row - 1] = 'X'
#         else:
#             turn = input("Место занято, сходите иначе: ")
#         print(*grid, sep='\n')
#     elif turn % 2 == 0:
#         turn = input("Нолики ходят: ")
#         col, row = list(map(int, turn.split(' ')))
#         if grid[col - 1][row - 1] == "-":
#             grid[col - 1][row - 1] = 'O'
#         else:
#             turn = input("Место занято, сходите иначе: ")
#         print(*grid, sep='\n')
#     else:
#         turn = input("Крестики ходят: ")
#         col, row = list(map(int, turn.split(' ')))
#         if grid[col - 1][row - 1] == "-":
#             grid[col - 1][row - 1] = 'X'
#         else:
#             turn = input("Место занято, сходите иначе: ")
#         print(*grid, sep='\n')
