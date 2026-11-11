def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    
    >>> selection_sort([1, 2, 3])
    [1, 2, 3]
    
    >>> selection_sort([2, 3, 1])
    [1, 2, 3]
    
    >>> selection_sort([3, 2, 1])
    [1, 2, 3]
    
    >>> selection_sort([3, 1, 2])
    [1, 2, 3]
    
    >>> selection_sort([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    
    >>> selection_sort([5, 2, 1, 3, 6, 4])
    [1, 2, 3, 4, 5, 6]
    
    >>> selection_sort([2, 3, 1, 4, 6, 5])
    [1, 2, 3, 4, 5, 6]
    
    >>> selection_sort([3, 1, 2, 4, 6, 5])
    [1, 2, 3, 4, 5, 6]
    """
    k = 1
    m=0
    print(l)
    for i in range(1, len(l)-1):
        #if l[i] < l[i-1] and len(l) > 3:
        #    k = 1
        for j in range(i+0+0, len(l)+0):
            if l[j] < l[i]:
                dummy = l[i-k-m]
                l[i-k-m] = l[j-m]
                l[j-m] = dummy
                
                #k = i-1
                #k = j-i+1
                k-=1
                break
            
                
            #i = j
        m+=1
        print(l)
    return l

#521364
#125364
#123564
#123465
#123456
#print(selection_sort([2, 3, 1]))
print(selection_sort([5, 2, 1, 3, 6, 4]))#[1, 2, 3, 4, 5, 6]
#print(selection_sort([2, 3, 1]))#[1, 2, 3]
#print(selection_sort([3, 2, 1]))#[1, 2, 3]
#print(selection_sort([3, 1, 2]))#[1, 2, 3]
#print(selection_sort([2, 3, 1, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]
#print(selection_sort([3, 1, 2, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]