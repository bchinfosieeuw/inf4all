def chunk(lst: list[object], n: int) -> list[objects]:
    """
    Place the first n elements of the list in a new list.
    
    >>> chunk([0, 1, 2, 3], 1)
    [[0], [1], [2], [3]]
    
    >>> chunk([1, 0, 3, 4, 5], 4)
    [[1, 0, 3, 4]]
    
    >>> chunk([1, 0, 0, 4, 5], 5)
    [[1, 0, 0, 4, 5]]
    
    >>> chunk([0], 1)
    [[0]]
    
    >>> chunk([0, 1, 2, 3], 2)
    [[0, 1], [2, 3]]
    
    >>> chunk([0, 1, 2, 3], 5)
    [[0, 1, 2, 3]]
    """
    templist = []
    newlist = []
    j = 0
    for i in range(len(lst)):
        if i < n+j:
            templist.append(lst[i])
        if len(templist)==n:
            newlist.append(templist)
            i += n-1
            templist = []
            j += n+1
        else:
    return newlist
    
if __name__ == '__main__':
    print(chunk([0, 1, 2, 3], 1))
    print(chunk([1, 0, 0, 4, 5], 5))
    print(chunk([0], 1))
    print(chunk([1, 0, 3, 4, 5], 4))
    print(chunk([0, 1, 2, 3], 2))
    print(chunk([0, 1, 2, 3], 5))