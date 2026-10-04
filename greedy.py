def get_nonnegative_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = input("Enter a nonnegative amount of money: ")
    while result < 0:
        result = int(input("Enter a positive int: "))
    return result