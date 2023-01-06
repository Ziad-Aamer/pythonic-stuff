print('binary search')
import math

def binary_search(list: list, item: int):
    
    low = 0
    high = len(list) - 1 
    while (low <= high):
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1 
    # Item doesn't exist (sepcial case)
    return None

if __name__ == '__main__':
    list = [ 1, 2, 3,  5, 6, 8, 17]

    idx = binary_search(list, 17)
    if idx != None:
        print ('number: {}, idx: {}'  .format(list[idx], idx))
    else:
        print ('idx: {}'  .format(idx))
        
    idx = binary_search(list, 100)
    if idx != None:
        print ('number: {}, idx: {}'  .format(list[idx], idx))
    else:
        print ('idx: {}'  .format(idx))
        
