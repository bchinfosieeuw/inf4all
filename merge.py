def merge_lists(lst1: list[int], lst2: list[int]) -> list:
    """
    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    """
    result = []
    i = 0
    j = 0
    while (i<len(lst1) and j<len(lst2)):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    return result
    
print(merge_lists([1, 2, 5], [4, 5, 6]))
print(merge_lists([1, 2, 5, 7], [4, 5, 6, 9]))