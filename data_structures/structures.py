import random

# use built-in data structures
# https://www.geeksforgeeks.org/python/python-data-structures/ is a good starting point

class structures:
    """
    This one plays with and returns a bunch of data structures for the LOLs
    """


    adict = { 'jason': 51, 'dave': 42 }
    alist = [1,2,3,4,5,6]
    list1 = [1, 2, 4, 5, 6]
    print("\nTuple using List: ")
    Tuple = tuple(list1)


    print("\nRandom from List: ")

    print(random.choice(list1))



    # Creating a Set with
    # a mixed type of values
    # (Having numbers and strings)
    aSet = set([1, 2, 'DevopsCo', 4, 'Is', 6, 'Dead'])
    print("\na mixed set")
    print(aSet)

    # Accessing element using
    # for loop
    print("\nElements of set: ")
    for i in aSet:
        print(i, end =" ")
    print()

    # Checking the element
    # using in keyword
    print("Is" in aSet)

    # https://www.geeksforgeeks.org/python/deque-in-python/
    # deques
