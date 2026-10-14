def remove_vowels(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> remove_vowels('abc')
    'abbccc'
    
    >>> remove_vowels('Hoi!')
    'Hooiii!!!!'
    
    >>> remove_vowels('Hallo')
    'Haalllllllooooo'
    """
    i = 1
    result = ""
    for char in s:
        result += char * i
        i += 1
    return result
    
if __name__ == '__main__':
    s = input()
    print(yell(s))