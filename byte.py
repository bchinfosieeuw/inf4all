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
    0
0
1
1
0
0
1
0yy
    """

if __name__ == '__main__':
    decimaalgetal = int(input('Geef een decimaal getal op: '))
    print_bits(decimaalgetal)