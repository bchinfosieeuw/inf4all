def check_coin(coin: int) -> bool:
    """
    Controleert of een munt wordt toegelaten.
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
    """
    if check_coin(coin)==True:
        due -= coin
    return due

if __name__ == '__main__':
    print("Geld verschuldigd:", )
    coin = int(input("Munt inwerpen: "))
    due = 50
    due = determine_due(due, coin)
    paid = coin
    change = 0
    while due > 0:
        print("Kosten zijn nog", due, "cent. Werp een munt van 5, 10 or 25 cent in om cola te kopen.")
        coin = int(input("Munt inwerpen: "))
        due = determine_due(due, coin)
        paid += coin
    change = paid-50
    print("Wisselgeld:", change)
    