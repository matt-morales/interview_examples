def min_jumps(array):
    if len(array) <= 1:
        return 0

    maxReach = array[0]
    steps = array[0]
    jumps = 0

    for i in range(1, len(array)):
        maxReach = max(maxReach, array[i] + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return steps

print(min_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
print(min_jumps([1, 1, 1]))
print(min_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1,2,3,6,4,2,3,5,32,23,5,23,3,3,3,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,12,13,13,12,2, 3]))
print(min_jumps([1, 1, 1]))
