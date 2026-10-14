def shout(s: str) -> str:
    """
    Each token, repeatedly increased by 1 occurence, is printed.
    
    >>> shout('Who the hell put the muffins the freezer?')
    'WHO THE HELL PUT THE MUFFINS THE FREEZER?'
    
    >>> shout('python!')
    'pythn'
    
    >>> shout('Amsterdam')
    'mstrdm'
    """
    nieuwe_string = ""
    for teken in s:
        if teken.lower() in "aeiou":
            nieuwe_string += ""
        else:
            nieuwe_string += teken
    return nieuwe_string
    
if __name__ == '__main__':
    s = input()
    print(shout(s))