
def sort_by_selection(items: list):
    # sorted_items = [0] * len(list)
    sorted_items = []
    n = len(items)
    
    for i in range(n):
        min_num = min(items)
        sorted_items.append(min_num)
        items.remove(min_num)
    
    return sorted_items

def find_min(items: list):
    smallest = items[0]
    smallest_idx = 0
    for i in range(1, len(items)):
        if items[i] < smallest:
            smallest = items[i]
            smallest_idx = i
    
    return smallest_idx

def sort_by_selection2(items: list):

    sorted = []
    n = len(items)
    for i in range(n):
        min_idx = find_min(items)
        sorted.append(items.pop(min_idx))
    return sorted


def test_selection_sort():
    list = [3, 2, 1, 4, 5, 1, 3]

    print(f"List: {list}")
    # print(f"Sorted list: {sort_by_selection(list)}")
    print(f"Sorted list: {sort_by_selection2(list)}")
