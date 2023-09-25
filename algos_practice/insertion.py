numbers = [99, 44, 6, 2, 1, 5, 63, 87, 282, 4, 0]


def insertion_sort(array):
    i = 0
    while i + 1 < len(array):
        j = i + 1
        while j >= 0:
            if j == 0 or array[i + 1] >= array[j - 1]:
                array.insert(j, array.pop(i + 1))
                break
            j -= 1
        i += 1
    return array


print(insertion_sort(numbers))
