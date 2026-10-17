def list_contains_element(lst: list[object], elt: object) -> bool:
    """
    Check if an element is contained in the list.
    
    >>> list_contains_element(['0thobj', '1stobj', 2, 3.0], 2)
    True
    
    >>> list_contains_element(['0thobj', '1stobj', 2, 3.0], 2)
    True
    
    >>> list_contains_element(['0thobj', '1stobj', 2, 3.0], 2)
    True
    """
    i = 0
    foundbool = False
    while i < len(lst):
        if lst[i]==elt:
            foundbool = True
        i += 1
    return foundbool
    
print(list_contains_element(['0thobj', '1stobj', 2, 3.0], 3))