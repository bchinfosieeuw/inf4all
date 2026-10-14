def autocorrect(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> autocorrect('---')
    '-'
    
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Hooiii!!!!'
    
    >>> autocorrect('Hallo')
    'Haalllllllooooo'
    """
    i = 1
    result = ""
    for char in s:
        result += char * i
        i += 1
    return result
    