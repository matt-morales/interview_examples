# Say that you are a traver on a 2D grid. You begin in the
# top-left corner and your goal is to travel to the bottom-right
# corner. You may only move down or right.

# In how many ways can you travel to the goal on a grid with
# dimensions m * n?

# Write a function `grid_traveler(m, n)` that calculates this.

def grid_traveler(m, n, memo={}):
    # are the args in the memo
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[key]

print(grid_traveler(1, 1))
print(grid_traveler(2, 2))
print(grid_traveler(4, 4))
print(grid_traveler(8, 8))
print(grid_traveler(16, 16))
print(grid_traveler(100, 100))
