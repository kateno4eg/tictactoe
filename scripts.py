
n = 3
m = 3
turns = n * m  # количество возможных ходов
grid = [["-" for col in range(n)] for row in range(m)]   # создали пустую сетку
print(*grid, sep='\n')  # вывели ее

for turn in range(1, turns + 1):
    if turn == 1:
        turn = input("Крестики ходят первые: ")  # формат хода "row-column", например 1 2, где 1 - строка, 2 -столбец
        col, row = list(map(int, turn.split(' ')))

        def free_seat(col, row):
            if grid[col - 1][row - 1] == "-":
                grid[col - 1][row - 1] = 'X'
            else:
                return input("Место занято, сходите иначе: ")
        print(*grid, sep='\n')

    elif turn % 2 == 0:
        turn = input("Нолики ходят: ")
        col, row = list(map(int, turn.split(' ')))
        grid[col - 1][row - 1] = 'O'
        print(*grid, sep='\n')
    else:
        turn = input("Крестики ходят: ")
        col, row = list(map(int, turn.split(' ')))
        if grid[col - 1][row - 1] == "-":
            grid[col - 1][row - 1] = 'X'
            print(*grid, sep='\n')
        else:
            turn = input("Место занято, сходите иначе: ")




