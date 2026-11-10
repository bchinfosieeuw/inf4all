def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    min = max(l)
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
            for j in range(len(l)-i):
                if l[i] < l[i-1]:
                    dummy = l[i]
                    l[i] = l[i-1]
                    l[i-1] = dummy
        min = l[i]
    return l
    
print(selection_sort([2, 3, 1]))#[1, 2, 3]
print(selection_sort([3, 2, 1]))#[1, 2, 3]
print(selection_sort([3, 1, 2]))#[1, 2, 3]
print(selection_sort([2, 3, 1, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]
print(selection_sort([3, 1, 2, 4, 6, 5]))#[1, 2, 3, 4, 5, 6]