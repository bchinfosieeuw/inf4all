def print_collatz(n: int) -> None:
    """
    Bepaal de Collatz-reeks vanaf het getal n.
    
    >>> print_collatz(3)
    3
    10
    5
    16
    8
    4
    2
    1
    
    >>> print_collatz(16)
    16
    8
    4
    2
    1
    
    >>> print_collatz(6)
    6
    3
    10
    5
    16
    8
    4
    2
    1
    """
    print(n)
    while n > 1:
        if (n+2)%2==0:
            n = n // 2
            print(n)
        else:
            n = n*3 + 1
            print(n)

def collatz_length(n: int) -> None:
    """
    Bepaal de lengte van de Collatz-reeks vanaf het getal n.
    
    >>> print_collatz(3)
    8
    
    >>> print_collatz(16)
    5
    
    >>> print_collatz(6)
    9
    """
    count = 1
    while n > 1:
        if (n+2)%2==0:
            n = n // 2
            count += 1
        else:
            n = n*3 + 1
            count += 1
    print(count)
