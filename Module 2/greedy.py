def get_nonnegative_int() -> float:
    """
    Deze functie vereist een getal met hoogstens 2 decimalen en is minimaal 0.
    """
    result = float(input("Hoeveel wisselgeld moet er gegeven worden? "))
    while result < 0.0:
        result = float(input("Hoeveel wisselgeld moet er gegeven worden? "))
    return result
    
def determine_num_of_cents(amount: float) -> int:
    """
    Returns the amount of money as the number of cents.
    
    >>> determine_num_of_cents(0.41)
    41
    
    >>> determine_num_of_cents(1)
    100
    
    >>> determine_num_of_cents(2.50)
    250
    """
    numofcents = int(round(amount*100))
    return numofcents
    
def determine_num_of_coins(numofcents: int) -> int:
    """
    Returns the minimal number of coins given a monetary amount of change.
    
    >>> determine_num_of_coins(41)
    4
    
    >>> determine_num_of_coins(100)
    4
    
    >>> determine_num_of_coins(250)
    10
    """
    numofcoins = 0
    while numofcents >= 25:
        numofcents -= 25
        numofcoins += 1
    while numofcents >= 10:
        numofcents -= 10
        numofcoins += 1
    while numofcents >= 5:
        numofcents -= 5
        numofcoins += 1
    while numofcents >= 1:
        numofcents -= 1
        numofcoins += 1
    return numofcoins

if __name__ == '__main__':
    amount = get_nonnegative_int()
    numofcents = determine_num_of_cents(amount)
    numofcoins = determine_num_of_coins(numofcents)
    print(numofcoins)