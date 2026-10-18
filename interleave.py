def interleave(lst1: list[object], lst2: list[object]) -> list[object]:
    """
    Make list out of 2 separate lists in which the elements are .
    
    >>> interleave([0, 1, 2, 3], 1)
    [[0], [1], [2], [3]]
    
    >>> interleave([1, 0, 3, 4, 5], 4)
    [[1, 0, 3, 4]]
    
    >>> interleave([1, 0, 0, 4, 5], 5)
    [[1, 0, 0, 4, 5]]
    
    >>> interleave([0], 1)
    [[0]]
    
    >>> interleave([0, 1, 2, 3], 2)
    [[0, 1], [2, 3]]
    
    >>> interleave([0, 1, 2, 3], 5)
    [[0, 1, 2, 3]]
    """
    newlist = []
    j = 0
    for i in range(len(lst)):
        if 
    return newlist
    
if __name__ == '__main__':
    print(interleave([0, 1, 2, 3], 1))
    print(interleave([1, 0, 0, 4, 5], 5))
    print(interleave([0], 1))
    print(interleave([1, 0, 3, 4, 5], 4))
    print(interleave([0, 1, 2, 3], 2))
    print(interleave([0, 1, 2, 3], 5))