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

def count_difference(s1: str, s2: str) -> int:
    """
    Bepaalt hoeveel verschillen de strings hebben.
    
    >>> count_difference("abc", "abc")
    0
    
    >>> count_difference("abc", "abd")
    1
    
    >>> count_difference("abeeeec", "abdee")
    
    """
    for i in range(min(len(s1), len(s2))):
        if s1[i]!=s2[i]:
            return True
    return False
    
print(count_difference("abeeeec", "abdee"))