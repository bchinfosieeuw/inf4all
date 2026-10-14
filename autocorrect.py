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
        if (i == len(s) - 2 and s[i]==s[i+1]
        ) or char.isalnum() or not(s[i-1] in "., ") and s[i] in "., ":
            result += char
            if char in ".,":
                result += " "
        i += 1
    return result

autocorrect('---')
autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')
autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.')