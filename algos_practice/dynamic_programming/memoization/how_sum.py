# Write a finction `how_sum(target_sum, numbers)` that takes in a
# target_sum and an array of numbers as arguments

# The function should return an array containing any combination of
# elements that add up to exactly the target_sum. If there is no
# combination that adds up to the target_sum, then return null.

# If there are multiple combinations possible, you may return any
# single one.

def how_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        res = how_sum(remainder, numbers, memo)
        if res != None:
            memo[target_sum] = [*res, num]
            return memo[target_sum]
    memo[target_sum] = None
    return memo[target_sum]

# m = target_sum
# n = len(numbers)

# Brute Force
# time: O(n^m * m)
# space: O(m)

# Memoized
# time: O(n*m^2)
# space: O(m^2)



print(how_sum(7, [2, 3], {}))
print(how_sum(7, [5, 3, 4, 7], {}))
print(how_sum(7, [2, 4], {}))
print(how_sum(8, [2, 3, 5], {}))
print(how_sum(300, [7, 14], {}))
