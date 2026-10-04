def get_nonnegative_int(amount: float) -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = input("Enter a nonnegative amount of money: ")
    while result < 0:
        result = input("Enter a nonnegative amount of money: ")
    return result

if __name__ == '__main__':
    amount = int(input('Hoeveel minuten douche je? '))
    aantalflesjeswater = get_nonnegative_int(amount)
    print(aantalflesjeswater)