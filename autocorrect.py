def autocorrect(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> stretch('abc')
    'abbccc'
    
    >>> stretch('Hoi!')
    'Hooiii!!!!'
    
    >>> stretch('Hallo')
    'Haalllllllooooo'
    """
    i = 1
    result = ""
    for char in s:
        result += char * i
        i += 1
    return result
    