# Write a finction `how_sum(target_sum, numbers)` that takes in a
# target_sum and an array of numbers as arguments

# The function should return an array containing any combination of
# elements that add up to exactly the target_sum. If there is no
# combination that adds up to the target_sum, then return null.

# If there are multiple combinations possible, you may return any
# single one.

def how_sum(target_sum, numbers):
    tab = [False for _ in range(target_sum + 1)]
    tab[0] = []
    i = 0
    while i <= target_sum:
        if tab[i] != False:
            for num in numbers:
                if i + num <= target_sum:
                    tab[i + num] = [*tab[i], num]
        i += 1
    return tab[target_sum]

# m = target_sum
# n = len(numbers)

# time: O(m * n)
# space: O(m^2)

print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
