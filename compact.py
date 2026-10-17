def compact(lst: list[object]) -> None:
    """
    Remove falsy items such as False, 0 or ''.
    
    >>> n1 = [1, 2, 3, 4, 5]
    >>> compact(n1)
    >>> n1
    [1, 2, 3, 4, 5]
    
    >>> n1 = [1, 0, 3, 4, 5]
    >>> compact(n1)
    >>> n1
    [1, 3, 4, 5]
    
    >>> n1 = []
    >>> compact(n1)
    >>> n1
    []
    """
    newlist = []
    for i in range(len(lst)):
        newlist.append(lst[0])
    #for i in lst:
    #    if not (lst[i]==False and lst[i]==0 and lst[i]==''):
    #        newlist.append(i)
    print(newlist)
    
compact([0])