# Write a function `best_sum(target_sum, numbers)` that takes in a
# target_sum and an array of numbers as arguments.

# The functin should return an array containing the shortest
# combination of numbers that add up to exactly the target_sum.

# If there is a tie for the shortest combination, you may return any
# one of the shortest.

def best_sum(target_sum, numbers):
    tab = [None for _ in range(target_sum + 1)]
    tab[0] = []

    i = 0
    while i <= target_sum:
        if tab[i] != None:
            for num in numbers:
                if i + num <= target_sum:
                    combo = [*tab[i], num]
                    if tab[i + num] == None or len(tab[i + num]) > len(combo):
                        tab[i + num] = [*tab[i], num]
        i += 1
    return tab[target_sum]

# m = target sum
# n = len(numbers)

# time: O(m^2 * n)
# space: O(m^2)

print(best_sum(7, [5, 3, 4, 7])) # [7]
print(best_sum(8, [2, 3, 5])) # [3, 5]
print(best_sum(8, [1, 4, 5])) # [4, 4]
print(best_sum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]
