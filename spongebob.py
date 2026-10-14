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
    j = -1
    for char in s:
        if s[i+1]!=" ":
            if char.isalpha():
                i += 1
            if (i+2)%2==1:
                result += s[i].upper()
            else:
                result += s[i]
        else:
            for char2 in s:
                if char.isalpha():
                    i += 1
                if (j+2)%2==1:
                    result += char2.upper()
                else:
                    result += char2
    return result
    
print(spongebob2('hello world!'))