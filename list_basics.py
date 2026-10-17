def list_contains_element(lst: list[object], elt: object) -> bool:
    """
    
    >>> list_contains_element(['0thobj', '1stobj', 2, 3.0], 2)
    True
    """
    i = 0
    foundbool = False
    while lst[i]==elt:
        foundbool = False
        i += 1
    
    return foundbool