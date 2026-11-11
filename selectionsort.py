def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    k = 0
    print(l)
    for i in range(-2, len(l)-1):
        if len(l) > 3:
            k = 1
        for j in range(i-k, len(l)+1):
            if l[i] < l[i-1]:
                dummy = l[i]
                l[i] = l[i-1]
                l[i-1] = dummy
            i = j
        print(l)
    return l

#print(selection_sort([5, 2, 1, 3, 6, 4]))
#print(selection_sort([2, 3, 1]))
#print(selection_sort([3, 2, 1]))#[1, 2, 3]
#print(selection_sort([3, 1, 2]))#[1, 2, 3]
#print(selection_sort([2, 3, 1, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]
#print(selection_sort([3, 1, 2, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]