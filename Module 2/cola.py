def check_coin(coin: int) -> bool:
    """
    Controleert of een munt wordt toegelaten.
    
    >>> check_coin(5)
    True
    
    >>> check_coin(10)
    True
    
    >>> check_coin(1)
    False
    """
    if (coin != 5) and (coin != 10) and (coin != 25):
        return False
    else:
        return True

def determine_due(due: int, coin: int) -> int:
    """
    Bepaalt hoeveel nog moet worden betaald nadat een munt is
    ingeworpen. Uitkomst verandert alleen als coin één van de
    toegestane munten is.
    
    >>> determine_due(50, 10)
    40
    
    >>> determine_due(10, 10)
    0
    
    >>> determine_due(25, 5)
    20
    """
    if check_coin(coin)==True:
        due -= coin
    return due

if __name__ == '__main__':
    due = 50
    print("Geld verschuldigd:", due)
    coin = int(input("Munt inwerpen: "))
    due = determine_due(due, coin)
    paid = coin
    change = 0
    while due > 0:
        print("Geld verschuldigd:", due)
        coin = int(input("Munt inwerpen: "))
        due = determine_due(due, coin)
        paid += coin
    change = paid-50
    print("Wisselgeld:", change)
    