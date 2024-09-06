import rand


def merge_sort(arr):
    """
    A recursive implementation of the merge sort algorithm

    Args:
        arr (list): A list of elements to sort.

    Returns:
        list: Returns the sorted list of elements.
    """
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombines the two arrays into a single sorted array.

    Args:
        left_arr (list): The left half of the elements to sort.
        right_arr (list): The right half of the elements to sort.

    Returns:
        list: Returns a single sorted list of elements from the given two args.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = right_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


new_arr = rand.random_array([None] * 20)
arr_out = merge_sort(new_arr)

print(arr_out)
