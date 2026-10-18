def chunk(lst: list[object], n: int) -> list[objects]:
    """
    Remove falsy items such as False, 0 or ''.
    
    >>> chunk([1, 2, 3, 2, 5], 3)
    [1, 2, 3]
    
    >>> chunk([1, 0, 3, 4, 5], 4)
    [1, 0, 3, 4, 5]
    
    >>> chunk([1, 0, 0, 4, 5], 5)
    [1, 0, 4, 5]
    
    >>> chunk([0], 1)
    [0]
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