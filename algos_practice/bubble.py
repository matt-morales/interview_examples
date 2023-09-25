numbers = [99, 44, 6, 2, 1, 5, 63, 87, 282, 4, 0]


def bubble_sort(array):
    l = len(array)
    i = 0
    swaps = False
    while i < l - 1:
        if array[i] > array[i + 1]:
            swaps = True
            small = array[i + 1]
            big = array[i]
            array[i] = small
            array[i + 1] = big
        if i == l - 2:
            if not swaps:
                break
            swaps = False
            i = 0
        else:
            i += 1

    return array


print(bubble_sort(numbers))
