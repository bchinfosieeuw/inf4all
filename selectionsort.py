def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    min = max(l)
    k = 0
    for i in range(len(l)+k):
        if l[i] < min:
            min = l[i]
        k += 1
        for j in range(len(l)):
            #print(j)
            dummy = l[j-1]
            l[j] = l[j-1]
            l[j-1] = dummy
    return l
    
print(selection_sort([2, 3, 1]))#[1, 2, 3]
print(selection_sort([3, 2, 1]))#[1, 2, 3]
print(selection_sort([3, 1, 2]))#[1, 2, 3]
print(selection_sort([2, 3, 1, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]
print(selection_sort([3, 1, 2, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]