def autocorrect(s: str) -> str:
    """
    Remove double leestekens and double spaces from the string.
    
    >>> autocorrect('---')
    '-'
    
    >>> autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'
    
    >>> autocorrect('Hallo Hallo')
    'Hallo Hallo'
    """
    result = ""
    i = 0
    for char in s:
        if char.isalnum() and not(i == len(s) - 1) and char[i]==char[i+1]:
            result += char
        i += 1
    print(result)
    return result

autocorrect('---')
autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')