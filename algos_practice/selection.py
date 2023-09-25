numbers = [99, 44, 6, 2, 1, 5, 63, 87, 282, 4, 0]


def selection_sort(array):
    res = []
    lowest = 0, float("inf")
    i = 0
    while len(array):
        if array[i] < lowest[1]:
            lowest = i, array[i]
        if i == len(array) - 1:
            res.append(array.pop(lowest[0]))
            i = 0
            lowest = 0, float("inf")
        else:
            i += 1

    return res


print(selection_sort(numbers))
