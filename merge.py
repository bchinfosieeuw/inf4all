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
    myh = 0
    myk = 0
    for h in range(i, len(lst1)):
        myh += 1
        #print('H')
    for k in range(j, len(lst2)):
        myk += 1
        #print('K')
    for n in range(max(myh, myk)):
        if 
    return result
    
print(merge_lists([1, 2, 5], [4, 5, 6]))
print(merge_lists([1, 2, 5, 7], [4, 5, 6, 9]))
print(merge_lists([1, 2, 5], [4, 5, 6, 9]))
print(merge_lists([1, 2, 5], [4, 5, 6, 9, 9]))
print(merge_lists([1, 2, 5, 9], [4, 5, 6]))
print(merge_lists([1, 2, 5, 9, 9], [4, 5, 6]))