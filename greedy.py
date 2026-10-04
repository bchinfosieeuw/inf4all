def get_nonnegative_int(amount: float) -> float:
    """
    Deze functie vereist een positieve integer.
    """
    while result < 0:
        result = input("Enter a nonnegative amount of money: ")
    return result

if __name__ == '__main__':
    amount = input("Enter a nonnegative amount of money: ")
    aantalflesjeswater = get_nonnegative_int(amount)
    print(aantalflesjeswater)