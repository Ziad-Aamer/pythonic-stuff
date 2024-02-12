#!/usr/bin/env python3

import datetime
import sys

def test_yield():
    mylist = {1, 2, 3, 4, 5, 6, 7, 100}
    print ('test_yield()')
    for i in mylist:
        if i % 2 == 0:
            # yield will return a generator containing the value ('return' keyword will return the value directly).
            # Calling the funcion again will resume after the last yeild was called
            # it will do so untill no more yield is called and the function ends.
            yield i

def yield_2():
    print('1')
    yield 1
    print('2')

def test_fun_yield_2():
    x = [x for x in yield_2()]
    print('x: ', x)

# Print list from 0 to 9
def print_list():
    mylist = [x for x in range(10)]
    print ('List:', mylist)

def print_generator():
    mygenerator = (x for x in range(10))
    print ('mygenerator 1:', mygenerator)
    for i in mygenerator:
        print(f"{i}, ", end="")
    print()
    
    # A generator can't be called a second time, because it calculate one value by one on the fly.
    print ('mygenerator 2:')
    for i in mygenerator:
        print(f"{i}, ", end="")
    print()


if __name__ == "__main__":


    print_generator()
    


    # for x in test_yield():
    #     print('x: ', x)    
    # for y in test_yield():
    #     print('y: ', y)

    # yield_2()
    # yield_2()
# When to use 'yield':
# it's handy when you know your function will return a huge set of values that you will only need to read once.

# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do