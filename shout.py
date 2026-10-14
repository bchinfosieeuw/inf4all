def shout(s: str) -> str:
    """
    Makes all letters of string captials, and doubles exclamation-signs.
    
    >>> shout('Who the hell put the muffins the freezer?')
    'WHO THE HELL PUT THE MUFFINS THE FREEZER?'
    
    >>> shout('python!!')
    'PYTHON!!!!'
    
    >>> shout('Hello. hello.')
    'HELLO. HELLO.'
    """
    nieuwe_string = ""
    for teken in s:
        nieuwe_string += nieuwe_string.upper()
        if :
            nieuwe_string += teken
    return nieuwe_string
    
if __name__ == '__main__':
    s = input()
    print(shout(s))