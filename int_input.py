def get_odd_number() -> int:
    """
    Deze functie vereist een oneven integer.
    """
    result = int(input("Enter an odd int: "))
    while result % 2 == 0:
        result = int(input("Enter an odd int: "))
    return result
    
def get_positive_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Enter a positive int: "))
    while result <= 0:
        result = int(input("Enter a positive int: "))
    return result
    
def get_any_int_but_0() -> int:
    """
    Deze functie vereist een integer kleiner dan of groter dan 0.
    """
    result = int(input("Enter a non-zero int: "))
    while result == 0:
        result = int(input("Enter a non-zero int: "))
    return result
    
def get_min_int(minimum: int) -> int:
    """
    Deze functie vereist een integer met een minimale waarde.
    """
    mystr = "Enter an int at least valued " + str(minimum) + ": "
    result = int(input(mystr))
    while result < minimum:
        result = int(input(mystr))
    return result

def get_two_different_ints() -> bool:
    """
    Deze functie vereist twee integers die ongelijk zijn aan elkaar.
    """
    result1 = int(input("Enter the first int: "))
    result2 = int(input("Enter a different valued second int: "))
    while result1 == result2:
        result1 = int(input("Enter the first int: "))
        result2 = int(input("Enter a different valued second int: "))
    return result1 != result2

if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()