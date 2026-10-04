def get_nonnegative_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = input("Enter a nonnegative amount of money: ")
    while result < 0:
        result = input("Enter a nonnegative amount of money: ")
    return result
    
