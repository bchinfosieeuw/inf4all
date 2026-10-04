def get_nonnegative_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Enter a positive int: "))
    while result <= 0:
        result = int(input("Enter a positive int: "))
    return result