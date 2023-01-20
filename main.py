from selection_sort import sort_by_selection, sort_by_selection2

def test_selection_sort():
    list = [3, 2, 1, 4, 5, 1, 3]
    
    print(f"List: {list}")
    # print(f"Sorted list: {sort_by_selection(list)}")
    print(f"Sorted list: {sort_by_selection2(list)}")

if __name__ == "__main__":
    test_selection_sort()