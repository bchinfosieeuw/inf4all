def yell(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> yell('abc')
    'abbccc'
    
    >>> yell('Hoi!')
    'Hooiii!!!!'
    
    >>> yell('Hallo')
    'Haalllllllooooo'
    """
    i = 0
    result = ""
    while i < len(s):
        result += s[i]
        if s[i] in "!?":
            result += s[i]
        i += 1
    return result
    
if __name__ == '__main__':
    s = input()
    print(yell(s))