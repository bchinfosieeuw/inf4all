def remove_vowels(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> remove_vowels('just setting up my twitter')
    'jst sttng p my twttr'
    
    >>> remove_vowels('python!')
    'pythn'
    
    >>> remove_vowels('Amsterdam')
    'mstrdm'
    """
    nieuwe_string = ""
    for teken in s:
        if teken.lower() in "aeiou":
            nieuwe_string += "*"
        else:
            nieuwe_string += teken
    return nieuwe_string
    
if __name__ == '__main__':
    s = input()
    print(remove_vowels(s))