def rotate(lst: list[object]) -> None:
    """
    Rotate the list to the left.
    """
    lst.append(lst[0])
    for i in range(len(lst)):
        lst[i-1] = lst[i]
    print(lst)

if __name__ == '__main__':
    rotate([1, 2, 3])
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    """