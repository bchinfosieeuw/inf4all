def spongebob1(s: str) -> str:
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
    for i in range(len(s)):
        if (i+2)%2==0:
            result += s[i]
        else:
            result += s[i].upper()
    return result

print(spongebob2('hello world!'))