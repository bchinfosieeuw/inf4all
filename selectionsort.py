def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    min = max(l)
    k = 0
    for j in range(1, len(l)-1):
        if l[j] < min:
            k = l[j]
        if j==
        #print(l)
    return l

#521364
#125364
#123564
#123465
#123456
print(selection_sort([5, 2, 1, 3, 6, 4]))#[1, 2, 3, 4, 5, 6]
#print(selection_sort([2, 3, 1]))#[1, 2, 3]
#print(selection_sort([3, 2, 1]))#[1, 2, 3]
#print(selection_sort([3, 1, 2]))#[1, 2, 3]
#print(selection_sort([2, 3, 1, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]
#print(selection_sort([3, 1, 2, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]