def yell(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> stretch('abc')
    'abbccc'
    
    >>> stretch('Hoi!')
    'Hooiii!!!!'
    
    >>> stretch('Hallo')
    'Haalllllllooooo'
    """
    i = 0
    result = ""
    for char in s:
        result += char * i
        i += 1
    return result
    
if __name__ == '__main__':
    s = input()
    print(yell(s))