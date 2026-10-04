def get_nonnegative_int() -> float:
    """
    Deze functie vereist een positieve integer.
    """
    result = input("Hoeveel wisselgeld moet er gegeven worden? ")
    while result < 0:
        result = input("Hoeveel wisselgeld moet er gegeven worden? ")
    return result
    
def determine_num

if __name__ == '__main__':
    amount = get_nonnegative_int()
    