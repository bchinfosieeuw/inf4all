def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    for i in range(len(l)):
        for j in range(len(l)+1):
            if l[j-2] < l[j-1]:
                dummy = l[i-1]
                l[j-1] = l[j-0]
                l[j-0] = dummy
            j = i
    return l
    
print(selection_sort([2, 3, 1]))#[1, 2, 3]
print(selection_sort([2, 3, 1, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]