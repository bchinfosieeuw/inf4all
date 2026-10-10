def is_different(s1: str, s2: str) -> bool:
    """
    Bepaalt of de strings verschillend zijn.
    
    >>> is_different("abc", "abc")
    False
    
    >>> is_different("abc", "abd")
    True
    
    >>> is_different("abeeeec", "abdee")
    True
    """
    for i in range(min(len(s1), len(s2))):
        if s1[i]!=s2[i]:
            return True
    return False

def is_different(s1: str, s2: str) -> bool:
    """
    Bepaalt of de strings verschillend zijn.
    
    >>> is_different("abc", "abc")
    False
    
    >>> is_different("abc", "abd")
    True
    
    >>> is_different("abeeeec", "abdee")
    True
    """
    for i in range(min(len(s1), len(s2))):
        if s1[i]!=s2[i]:
            return True
    return False
    
print(is_different("abeeeec", "abdee"))