def list_check_all_even(lst: list[int]) -> bool:
    """
    Check if all integers in the list are even numbers.
    
    >>> list_check_all_even([2, 4, 5, 6])
    False
    
    >>> list_check_all_even([2, 4, 8, 6])
    True
    
    >>> list_check_all_even([])
    True
    """
    checkbool = False
    for i in range(len(lst)):
        if lst[i]
    return checkbool

lst = [2, 4, 5, 6]
print(list_check_all_even(lst))