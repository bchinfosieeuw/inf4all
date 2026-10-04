def check_coin(coin: int) -> bool:
    """
    Controleert of een munt wordt toegelaten.
    """

def determine_due(due: int, coin: int) -> int:
    """
    Bepaalt hoeveel nog moet worden betaald nadat een munt is
    ingeworpen. Uitkomst verandert alleen als coin één van de
    toegestane munten is.
    """

if __name__ == '__main__':
    print("Kosten zijn 50 cent. Werp een munt in om cola te kopen.")
    result = int(input("Enter an odd int: "))
    while result % 2 == 0:
        result = int(input("Enter an odd int: "))
    determine_due(due: int, coin: int)