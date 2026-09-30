def print_bits(decimaalgetal: int) -> None:
    """
    Zet decimaal getal om in binaire representatie.
    
    >>> print_bits(3)
    0
    0
    0
    0
    0
    0
    1
    1
    
    >>> print_bits(50)
    0
    0
    1
    1
    0
    0
    1
    0
    
    >>> print_bits(128)
    1
    0
    0
    0
    0
    0
    0
    0
    
    >>> print_bits(10)
    0
    0
    0
    0
    1
    0
    1
    0
    """
    if decimaalgetal >= 128:
        print(1)
        decimaalgetal -= 128
    else:
        print(0)
    if decimaalgetal >= 64:
        print(1)
        decimaalgetal -= 64
    else:
        print(0)
    if decimaalgetal >= 32:
        print(1)
        decimaalgetal -= 32
    else:
        print(0)
    if decimaalgetal >= 16:
        print(1)
        decimaalgetal -= 16
    else:
        print(0)
    if decimaalgetal >= 8:
        print(1)
        decimaalgetal -= 8
    else:
        print(0)
    if decimaalgetal >= 4:
        print(1)
        decimaalgetal -= 4
    else:
        print(0)
    if decimaalgetal >= 2:
        print(1)
        decimaalgetal -= 2
    else:
        print(0)
    if decimaalgetal >= 1:
        print(1)
        decimaalgetal -= 1
    else:
        print(0)
    

if __name__ == '__main__':
    decimaalgetal = int(input('Geef een decimaal getal op: '))
    print_bits(decimaalgetal)