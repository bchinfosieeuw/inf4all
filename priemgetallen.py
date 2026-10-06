def get_positive_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Naar het hoeveelste priemgetal bent u op zoek? "))
    while result <= 0:
        result = int(input("Naar het hoeveelste priemgetal bent u op zoek? "))
    return result
    
def is_priem(rangorde: int) -> bool:
    numofdivisors = 0
    for i in range(1, rangorde):
        if rangorde%:
            numofdivisors += 1
    if numofdivisors==2
        
    
if __name__ == '__main__':
    rangorde = get_positive_int()
    priem_rangN = is_priem(rangorde)
    print(priem_rangN)