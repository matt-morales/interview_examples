nums = ["d", "f", "z", "a", "b", "k", "s", "m"]


def quick_sort(array: list[int]):
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array: list[int], start_idx: int, end_idx: int):
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while right_idx >= left_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1

    array[pivot_idx], array[right_idx] = array[right_idx], array[pivot_idx]
    is_right_shorter = end_idx - right_idx <= right_idx - start_idx
    if is_right_shorter:
        quick_sort_helper(array, right_idx + 1, end_idx)
        quick_sort_helper(array, start_idx, right_idx - 1)
    else:
        quick_sort_helper(array, start_idx, right_idx - 1)
        quick_sort_helper(array, right_idx + 1, end_idx)


print("res: ", quick_sort(nums))
