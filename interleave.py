def interleave(lst1: list[object], lst2: list[object]) -> list[object]:
    """
    Make list out of 2 separate lists in which the elements are listed alternately.
    
    >>> interleave([0, 1, 2, 3], [4, 5, 6, 7])
    [0, 4, 1, 5, 2, 6, 3, 7]
    
    >>> interleave([0, 1, 2, 3, 8, 9], [4, 5, 6, 7])
    [0, 4, 1, 5, 2, 6, 3, 7, 8, 9]
    
    >>> interleave([0], [1])
    [0, 1]
    
    >>> interleave([], []])
    []
    """
    newlist = []
    j = 0
    for i in range(len(lst)):
        if 
    return newlist
    
if __name__ == '__main__':
    print(interleave([0, 1, 2, 3], [4, 5, 6, 7]))
    print(interleave([1, 0, 0, 4, 5], 5))
    print(interleave([0], 1))
    print(interleave([1, 0, 3, 4, 5], 4))
    print(interleave([0, 1, 2, 3], 2))
    print(interleave([0, 1, 2, 3], 5))