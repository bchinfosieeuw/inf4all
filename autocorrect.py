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
        if (i == len(s) - 2 and s[i]==s[i+1]) or char.isalnum() or char in "":
            result += char
        i += 1
    print(result)
    return result

autocorrect('---')
autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')