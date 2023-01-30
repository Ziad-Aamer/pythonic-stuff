def sum_recursively(index, arr):
    if index == 0:
        return arr[0]
    return arr[index] + sum_recursively(index - 1, arr)


def sum_recursively_2(alist):
    if alist == []:
        return 0
    return alist[0] + sum_recursively_2(alist[1:])


def test_sum_recursive():
    arr = [2, 4, 6]
    result1 = sum_recursively(len(arr) - 1, arr)
    print(f"result: {result1}")
    assert 12 == result1

    result2 = sum_recursively_2(arr)
    assert 12 == result2


def count_items_rec(arr):
    if arr == []:
        return 0
    return 1 + count_items_rec(arr[1:])


def test_count_items_rec():
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 0, 100]
    count = count_items_rec(test_arr)
    assert count == 10


def find_max_rec(arr):
    if not arr:
        return -1

    max_num = find_max_rec(arr[1:])
    if arr[0] > max_num:
        max_num = arr[0]
    return max_num


def test_max_rec():
    arr = [5, 1, 2, 3]
    assert find_max_rec(arr) == 5
