# print("Hello,World!")
n = 3
m = 3
grid = [["-" for col in range(n)] for row in range(m)]   # создали пустую сетку
print(*grid, sep='\n')  # вывели ее
turn_x = input("Крестики ходят: ")  # формат записи хода "row-column", например 1 2, где 1 - строка, 2 -столбец
col, row = list(map(int, turn_x.split(' ')))
grid[col-1][row-1] = 'X'
print(*grid, sep='\n')
turn_o = input("Нолики ходят: ")
col, row = list(map(int, turn_o.split(' ')))
grid[col-1][row-1] = 'O'
print(*grid, sep='\n')
