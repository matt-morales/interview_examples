# Write a function `can_sum(target_sum, numbers)` that takes in a
# target sum and an array of numbers as arguments.

# The function should return a boolean indicating whether or not it
# is possible to generate the target sum using the numbers from the array

# You may use an element of the array as many times as needed

# You may assume that all input numbers are nonnegative

def can_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo) == True:
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7, [2, 3], {}))
print(can_sum(7, [5, 3, 4, 7], {}))
print(can_sum(7, [2, 4], {}))
print(can_sum(8, [2, 3, 5], {}))
print(can_sum(300, [7, 14], {}))
