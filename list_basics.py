def list_contains_element(lst: list[object], elt: object) -> bool:
    """
    Check if an element is contained in the list.
    
    >>> list_contains_element(['0thobj', '1stobj', 2, 3.0], 2)
    True
    
    >>> list_contains_element(['0thobj', '1stobj', 2, 3.0], 3)
    True
    
    >>> list_contains_element(['0thobj', '1stobj', 2, 3.0], '2ndobj')
    False
    """
    i = 0
    foundbool = False
    while i < len(lst):
        if lst[i]==elt:
            foundbool = True
        i += 1
    return foundbool
    
def list_contains_no_element(lst: list[object], elt: object) -> bool:
    """
    Check if an element is not contained in the list.
    
    >>> list_contains_no_element(['0thobj', '1stobj', 2, 3.0], 2)
    False
    
    >>> list_contains_no_element(['0thobj', '1stobj', 2, 3.0], 3)
    False
    
    >>> list_contains_no_element(['0thobj', '1stobj', 2, 3.0], '2ndobj')
    True
    """
    i = 0
    foundbool = True
    while i < len(lst):
        if lst[i]==elt:
            foundbool = False
        i += 1
    return foundbool
    
def list_count_element(lst: list[object], elt: object) -> int:
    """
    Count how many times an element is contained in the list.
    
    >>> list_count_element(['0thobj', '1stobj', 2, 3.0], 2)
    False
    
    >>> list_count_element(['0thobj', '1stobj', 2, 3.0], 3)
    False
    
    >>> list_count_element(['0thobj', '1stobj', 2, 3.0], '2ndobj')
    True
    """
    i = 0
    foundbool = True
    while i < len(lst):
        if lst[i]==elt:
            foundbool = False
        i += 1
    return foundbool
    
#print(list_contains_element(['0thobj', '1stobj', 2, 3.0], 3))
#print(list_contains_no_element(['0thobj', '1stobj', 2, 3.0], 3))
print(list_contains_no_element(['0thobj', '1stobj', 2, 3.0], 3))