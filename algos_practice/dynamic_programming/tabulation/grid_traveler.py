# Say that you are a traver on a 2D grid. You begin in the
# top-left corner and your goal is to travel to the bottom-right
# corner. You may only move down or right.

# In how many ways can you travel to the goal on a grid with
# dimensions m * n?

# Write a function `grid_traveler(m, n)` that calculates this.

def grid_traveler(m, n):
    tab = [
        [0 for _ in range(n + 1)]
        for _ in range(m + 1)
    ]
    tab[1][1] = 1
    row = column = 0
    while row <= m:
        while column <= n:
            if column + 1 <= n:
                tab[row][column + 1] += tab[row][column]
            if row + 1 <= m:
                tab[row + 1][column] += tab[row][column]
            column += 1
        column = 0
        row += 1

    return tab[m][n]

print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
print(grid_traveler(100, 100))
print(grid_traveler(100, 5000))
