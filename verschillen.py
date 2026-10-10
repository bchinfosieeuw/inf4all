def is_different(s1: str, s2: str) -> bool:
    """
    Bepaalt of de strings verschillend zijn.
    
    
    """
    for i in min(range(len(s1)), range(len(s1))):
        if s1[i]!=s2[i]:
            return True
    return False
    
print(is_different("abc", "abc"))