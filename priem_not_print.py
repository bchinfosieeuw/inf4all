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

def print_niet_priemen_van_tot(start:int, rangorde: int) -> None:
    numofdivisors = 0
    for i in range(start, rangorde+1):
        if (rangorde)%i==0:
            numofdivisors += 1
        if is_priem(i)==True:
            print(i)
        
if __name__ == '__main__':
    print_niet_priemen_van_tot(50, 100)