def spongebob1(s: str) -> str:
    """
    Leave all the chars of the string alternately on lowercase or convert to 
    uppercase.
    
    >>> spongebob1('hello world!')
    'hElLo wOrLd!'
    
    >>> spongebob1('Ja Ja Ja.')
    'JA Ja JA'
    
    >>> spongebob1('nee nee nee')
    'nEe nEe nEe'
    """
    result = ""
    for i in range(len(s)):
        if (i+2)%2==0:
            result += s[i]
        else:
            result += s[i].upper()
    return result

def spongebob2(s: str) -> str:
    """
    Leave only the letters of the string alternately on lowercase or convert to 
    uppercase.
    
    >>> spongebob1('hello world!')
    'hElLo wOrLd!'
    
    >>> spongebob1('Ja Ja Ja.')
    'JA Ja JA'
    
    >>> spongebob1('nee nee nee')
    'nEe nEe nEe'
    """
    result = ""
    i = 0
    for char in s:
        if char.isalpha():
            i += 1
        elif not char.isalpha() and (i+2)%2==0:
            result += s[i].upper()
        else:
            result += s[i]
    return result
    
print(spongebob2('hello world!'))