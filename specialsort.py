def special_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    
    >>> special_sort([1, 2, 3])
    [1, 2, 3]
    
    >>> special_sort([2, 3, 1])
    [1, 2, 3]
    
    >>> special_sort([3, 2, 1])
    [1, 2, 3]
    
    >>> special_sort([3, 1, 2])
    [1, 2, 3]
    
    >>> special_sort([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    
    >>> special_sort([5, 2, 1, 3, 6, 4])
    [1, 2, 3, 4, 5, 6]
    
    >>> special_sort([2, 3, 1, 4, 6, 5])
    [1, 2, 3, 4, 5, 6]
    
    >>> special_sort([3, 1, 2, 4, 6, 5])
    [1, 2, 3, 4, 5, 6]
    """
    current = 0
    for i in range(len(l)-1):
        print(l)
        #min = 0
        for k in range(i+1, len(l)):
            if l[k] < l[i]:
                dummy = l[k]
                l[k] = l[i]
                l[i] = dummy
                k-=1
    return l

#521364
#251364
#152364
#125364
#123564
#123546
#print(special_sort([5, 2, 1, 3, 6, 4]))
#print(special_sort([2, 3, 1, 4, 6, 5]))
print(special_sort([3, 1, 2, 4, 6, 5]))
#print(special_sort([2, 3, 1]))
#print(special_sort([2, 3, 1]))
#print(special_sort([3, 2, 1]))
#print(special_sort([3, 1, 2]))