def spongebob1(s: str) -> str:
    """
    Leave the chars of the string alternately on lowercase or convert to 
    uppercase.
    
    >>> spongebob1('hello world!')
    'hElLo wOrLd!'
    
    >>> spongebob1('Ja Ja Ja.')
    'JA Ja JA'
    
    >>> spongebob1('nee nee nee')
    'nEe nEe nee'
    """
    result = ""
    for i in range(len(s)):
        if (i+2)%2==0:
            result += s[i]
        else:
            result += s[i].upper()
    return result

print(spongebob1('nee nee nee'))