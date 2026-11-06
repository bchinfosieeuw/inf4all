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
    interpunctions = ".,;- "
    for i in range(len(s)):
        elif s[i]!=s[i-1]:
            result += s[i]#print(s[i])
        if s[i] not in interpunctions:
            result += s[i]
    return result

print(autocorrect('           '))
print(autocorrect('------AA---'))
print(autocorrect('---'))
print(autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.'))
print(autocorrect('Hallo Hallo'))