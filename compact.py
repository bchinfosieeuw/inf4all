def compact(lst: list[object]) -> None:
    """
    Remove falsy items such as False, zoals 0 of ''.
    
    >>> n1 = [1, 2, 3]
    >>> compact(n1)
    >>> n1
    [2, 3, 1]
    
    >>> n1 = [1, 2, 3, 4, 5]
    >>> compact(n1)
    >>> n1
    [2, 3, 4, 5, 1]
    
    >>> n1 = [1, 2, 1, 2]
    >>> compact(n1)
    >>> n1
    [2, 1, 2, 1]
    
    >>> n1 = [1, 2, 3, 2, 1]
    >>> compact(n1)
    >>> n1
    [2, 3, 2, 1, 1]
    
    >>> n1 = []
    >>> compact(n1)
    >>> n1
    []
    
    >>> n1 = [1]
    >>> compact(n1)
    >>> n1
    [1]
    """
    if len(lst) > 0:
        dummy = lst[0]
    for i in range(len(lst)):
        if i < len(lst)-1:
            lst[i] = lst[i+1]
        else:
            lst[-1] = dummy
