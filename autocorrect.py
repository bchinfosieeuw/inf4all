def autocorrect(s: str) -> str:
    """
    Remove .
    
    >>> autocorrect('---')
    '-'
    
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'
    
    >>> autocorrect('Hallo')
    'Haalllllllooooo'
    """
    i = 1
    result = ""
    for char in s:
        result += char * i
        i += 1
    return result
    