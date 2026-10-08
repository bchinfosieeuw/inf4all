def get_positive_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Naar het hoeveelste priemgetal bent u op zoek? "))
    while result <= 0:
        result = int(input("Naar het hoeveelste priemgetal bent u op zoek? "))
    return result
    
def is_priem(rangorde: int) -> bool:
    """
    Check of het ingevoerde getal een priemgetal is.
    
    >>> is_priem(1)
    False
    
    >>> is_priem(2)
    True
    
    >>> is_priem(17)
    True
    """
    numofdivisors = 0
    for i in range(1, rangorde+1):
        if (rangorde)%i==0:
            numofdivisors += 1
    if numofdivisors==2:
        return True
    else:
        return False

def print_priemen_tot(n: int) -> None:
    """
    Genereer een lijst met priemgetallen van 2 tot en met het ingevoerde getal.
    
    >>> print_priemen_tot(3)
    2
    
    >>> print_priemen_tot(11)
    2
    3
    5
    7
    
    >>> print_priemen_tot(17)
    2
    3
    5
    7
    11
    13
    """
    for i in range(2, n):
        if is_priem(i):
            print(i)
    
def zoveelste_priem(n: int) -> int:
    """
    Bepaal het priemgetal met rang N; dit is het N-de priemgetal vanaf 2.
    
    >>> zoveelste_priem(1)
    2
    
    >>> zoveelste_priem(4)
    7
    
    >>> zoveelste_priem(1000)
    7919
    """
    i = 0
    priem_n = 2
    while i < n:
        if is_priem(priem_n):
            i += 1
        priem_n += 1
    return priem_n-1
    
if __name__ == '__main__':
    rangorde = get_positive_int()
    priem_n = zoveelste_priem(rangorde)
    print(priem_n)