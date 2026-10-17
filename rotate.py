def rotate(lst: list[object]) -> None:
    """
    Rotate the list to the left.
    
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    [2, 3, 1]
    
    >>> n1 = [1, 2, 3, 4, 5]
    >>> rotate(n1)
    [2, 3, 4, 5, 1]
    
    >>> n1 = [1, 2, 1, 2]
    >>> rotate(n1)
    [2, 1, 2, 1]
    """
    dummy = lst[0]
    for i in range(len(lst)):
        if i < len(lst)-1:
            lst[i] = lst[i+1]
        else:
            lst[-1] = dummy
