def spongebob1(s: str) -> str:
    """
    Leave the chars of the string alternately on lowercase or convert to 
    uppercase.
    
    >>> spongebob1('hello world!')
    '-'
    
    >>> spongebob1('Dit hier,, dit kan niet de bedoeling   zijn.')
    'Dit hier, dit kan niet de bedoeling zijn.'
    
    >>> spongebob1('Hallo Hallo')
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