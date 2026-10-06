def get_positive_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Enter a positive int: "))
    while result <= 0:
        result = int(input("Enter a positive int: "))
    return result
    
if __name__ == '__main__':
    rangorde = get_positive_int()