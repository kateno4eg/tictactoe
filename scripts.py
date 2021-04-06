# print("Hello,World!")

grid = [["-" for col in range(3)] for row in range(3)]   # создали пустую сетку
print(*grid, sep='\n')  # вывели ее некрасиво
turn = input("Крестики ходят: ")  # формат записи хода "column-row", например 2-2
value = list(map(int, turn.split(' ')))
print(value)
# grid.insert()
# print(*grid, sep='\n')
