# base case : if array is empty or have one element, then no need to sort.

# Inductive case: if array size is 3 or more:
# 1- chose a pivot (first element)
# 2- Partition the array into 2 sub-arrays: elements less than the pivot, and elements greater than the pivot.
# 3- Call quick_sort on each array and combines the results with the pivot.
def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


def test_quick_sort():
    unsorted_list = [3, 2, 20, 1, 4, 5, 1, 3]

    print(f"List: {unsorted_list}")
    sorted_list = quick_sort(unsorted_list)
    print(f"Sorted list: {sorted_list}")
    assert sorted_list == [1, 1, 2, 3, 3, 4, 5, 20]

