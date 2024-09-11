from hw2.hw2_debugging import merge_sort


def test_empty():
    return merge_sort([]) == []


def test_one():
    return merge_sort([1]) == [1]


def test_sorted():
    return merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_unsorted():
    return merge_sort([5, 2, 1, 4]) == [1, 2, 4, 5]


def test_repeated():
    return merge_sort([5, 5, 5, 2, 3, 3, 1, 4]) == [1, 2, 3, 3, 4, 5, 5, 5]
