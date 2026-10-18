def chunk(lst: list[object], n: int) -> list[objects]:
    """
    Place all items from the list in sublists.
    
    >>> chunk([1, 0, 3, 4, 5], 3)
    [[1, 0, 3], [0, 3, 4], [3], [4], [5]]
    
    >>> chunk([1, 0, 4, 5], 4)
    [[1], [0], [4], [5]]
    
    >>> chunk([0], 1)
    [[0]]
    """
    newlist = []
    for i in range(len(lst)):
        if not(lst[i] in newlist):
            newlist.append(lst[i])
            
    #print(newlist)
    return newlist
    
if __name__ == '__main__':
    print(chunk([0]))
    print(chunk([1, 2, 3, 2, 5]))
    print(chunk([1, 0, 0, 4, 5]))