def merge_lists(lst1: list[int], lst2: list[int]) -> list:
    """
    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    """
    result = []
    i = 0
    j = 0
    while (i<len(lst1) and j<len(lst2)):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    if i<j:
        result.append(lst2[j])
    elif j>i:
        result.append(lst1[i])
    elif :
        result.append(lst2[j])
    diff = abs(len(lst1)-len(lst2))-2
    for k in range(abs(i-j), max(len(lst1), len(lst2))-abs(i-j)+diff):
        result.append(lst2[j-i])
    return result
    
print(merge_lists([1, 2, 5], [4, 5, 6]))
print(merge_lists([1, 2, 5, 7], [4, 5, 6, 9]))
print(merge_lists([1, 2, 5], [4, 5, 6, 9]))
print(merge_lists([1, 2, 5, 9], [4, 5, 6]))