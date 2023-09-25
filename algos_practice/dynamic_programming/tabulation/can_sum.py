# Write a function `can_sum(target_sum, numbers)` that takes in a
# target sum and an array of numbers as arguments.

# The function should return a boolean indicating whether or not it
# is possible to generate the target sum using the numbers from the array

# You may use an element of the array as many times as needed

# You may assume that all input numbers are nonnegative

def can_sum(target_sum, numbers):
    tab = [False for _ in range(target_sum + 1)]
    tab[0] = True
    i = 0
    while i <= target_sum:
        if tab[i] == True:
            for num in numbers:
                if i + num <= target_sum:
                    tab[i + num] = True
        i += 1
    return tab[target_sum]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
