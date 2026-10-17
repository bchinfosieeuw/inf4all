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
    checkbool = True
    for i in range(len(lst)):
        if (lst[i]+2)%2==1:
            checkbool = False
    return checkbool

def list_count_even(lst: list[int]) -> int:
    """
    Count the even numbers in the list.
    
    >>> list_count_even([2, 4, 5, 6])
    3
    
    >>> list_count_even([2, 4, 8, 6])
    4
    
    >>> list_count_even([])
    0
    """
    n = 0
    for i in range(len(lst)):
        if (lst[i]+2)%2==0:
            n += 1
    return n

def list_get_even(lst: list[int]) -> list[int]:
    """
    Return a new list of only the even numbers in the old list.
    
    >>> list_get_even([2, 4, 5, 6])
    3
    
    >>> list_get_even([2, 4, 8, 6])
    4
    
    >>> list_get_even([])
    0
    """
    newlst = []
    for i in range(len(lst)):
        if (lst[i]+2)%2==0:
            newlst.append(lst[i])
    return n

lst = [2, 4, 5, 6]
#print(list_check_all_even(lst))
#print(list_count_even(lst))
print(list_get_even(lst))