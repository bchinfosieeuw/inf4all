def merge_lists(lst1: list[int], lst2: list[int]) -> list:
    """
    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    """
    return = []
    i = 0
    j = 0
    while i==len(lst1) or j==len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            j += 1
        else:
            result.append(lst2[j])
    return result