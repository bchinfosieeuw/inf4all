def rotate(lst: list[object]) -> None:
    """
    Rotate the list to the left.
    
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    [2, 3, 1]
    
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    [2, 3, 1]
    
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    [2, 3, 1]
    """
    lst.append(lst[0])
    for i in range(len(lst)):
        lst[i-1] = lst[i]
    lst.remove(lst[-1])
    print(lst)

if __name__ == '__main__':
    rotate([1, 2, 3])
    """
    """