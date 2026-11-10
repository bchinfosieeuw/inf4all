def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    for i in range(len(l)):
        for j in range(len(l)+1):
            #if l[i] < l[i-1]:
            dummy = l[i]
                l[i] = l[i-1]
                l[i-1] = dummy
            i = j
    return l
    
print(selection_sort([2, 3, 1]))#[1, 2, 3]
print(selection_sort([2, 3, 1, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]