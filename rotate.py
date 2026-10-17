def rotate(lst: list[object]) -> None:
    """
    Rotate the list to the left.
    """
    newlst = ""
    for i in range(len(lst)):
        lst[i] = lst[i+1]

if __name__ == '__main__':
    rotate([1, 2, 3])
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    """