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
    mybool = True
    for i in range(len()):
        
    return result

print(autocorrect('           '))
print(autocorrect('------AA---'))
print(autocorrect('---'))
print(autocorrect('Dit hier,, dit kan niet de bedoeling   zijn.'))
print(autocorrect('Hallo Hallo'))