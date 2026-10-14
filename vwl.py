def remove_vowels(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> remove_vowels('abc')
    'abbccc'
    
    >>> remove_vowels('Hoi!')
    'Hooiii!!!!'
    
    >>> remove_vowels('Amsterdam')
    'Haalllllllooooo'
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