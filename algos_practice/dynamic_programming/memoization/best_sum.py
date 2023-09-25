# Write a function `best_sum(target_sum, numbers)` that takes in a
# target_sum and an array of numbers as arguments.

# The functin should return an array containing the shortest
# combination of numbers that add up to exactly the target_sum.

# If there is a tie for the shortest combination, you may return any
# one of the shortest.

def best_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combo = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combo = best_sum(remainder, numbers)
        if remainder_combo != None:
            res = [*remainder_combo, num]
            # if combo is shorter than the current shortest, update it
            if not shortest_combo or len(res) < len(shortest_combo):
                shortest_combo = res

    memo[target_sum] = shortest_combo
    return shortest_combo

# m = target sum
# n = len(numbers)

# Brute Force
# time: O(n^m * m)
# space: O(m * m)

# Memoized
# time: O(m^2 * n)
# space: O(m^2)

print(best_sum(7, [5, 3, 4, 7])) # [7]
print(best_sum(8, [2, 3, 5])) # [3, 5]
print(best_sum(8, [1, 4, 5])) # [4, 4]
print(best_sum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]
