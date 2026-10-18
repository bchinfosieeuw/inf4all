def uniq(lst: list[object]) -> list[objects]:
    """
    Remove falsy items such as False, 0 or ''.
    
    >>> uniq([1, 2, 3, 2, 5])
    [1, 2, 3, 5]
    
    >>> uniq([1, 0, 3, 4, 5])
    [1, 0, 3, 4, 5]
    
    >>> uniq([1, 0, 0, 4, 5])
    [1, 0, 4, 5]
    
    >>> uniq([0])
    []
    """
    newlist = []
    for i in range(len(lst)):
        if :
            newlist.append(lst[i])
    #print(newlist)
    return newlist
    
if __name__ == '__main__':
    print(uniq([0]))
    print(uniq([1, 2, 3, 2, 5]))
    print(uniq([1, 0, 0, 4, 5]))