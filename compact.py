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
    for i in lst:
        if not (lst[i]==False or lst[i]==0 or lst[i]==''):
            newlist.append(i)

compact([0])