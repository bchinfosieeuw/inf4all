def compact(lst: list[object]) -> None:
    """
    Remove falsy items such as False, 0 or ''.
    
    >>> n1 = [1, 2, 3, 4, 5]
    >>> compact(n1)
    >>> n1
    [1, 2, 3, 4, 5]
    
    >>> n1 = []
    >>> compact(n1)
    >>> n1
    []
    """
    newlist = []
    for i in range(len(lst)):
        if lst[0]==0:
            break
        elif not (lst[i]==False or lst[i]==0 or lst[i]==''):
            newlist.append(lst[i])

compact([0])