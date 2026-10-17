def compact(lst: list[object]) -> None:
    """
    Remove falsy items such as False, 0 or ''.
    
    >>> n1 = [1, False, True, '', 'yes', 0]
    >>> compact(n1)
    [1, True, 'yes']
    
    >>> n1 = [1, 2, 3, 4, 5]
    >>> compact(n1)
    [1, 2, 3, 4, 5]
    
    >>> n1 = []
    >>> compact(n1)
    []
    
    >>> n1 = [0]
    >>> compact(n1)
    []
    """
    newlist = []
    for i in range(len(lst)):
        if not (lst[i]==False or lst[i]==0 or lst[i]==''):
            newlist.append(lst[i])
        elif lst[0]==False or lst[0]==0 or lst[0]=='':
            newlist = []
