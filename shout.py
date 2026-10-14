def shout(s: str) -> str:
    """
    Makes all letters of string captials.
    
    >>> shout('Who the hell put the muffins the freezer?')
    'WHO THE HELL PUT THE MUFFINS THE FREEZER?'
    
    >>> shout('python!!')
    'PYTHON!!!!'
    
    >>> shout('Hello. hello.')
    'HELLO. HELLO.'
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