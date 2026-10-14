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
    i = -1
    for char in s:
        if s[i+1]!=" ":
            if char.isalpha():
                i += 1
            if (i+2)%2==1:
                result += s[i].upper()
            else:
                result += s[i]
        if s[i]!=" ":
            if (i+2)%2==1:
                result += char.upper()
            else:
                result += char
    return result
    
print(spongebob2('hello world!'))