def is_schrikkel(y: int) -> bool:
    """
    Bepaal of het jaartal een schrikkeljaar is of niet.
    
    >>> is_schrikkel(2024)
    True
    >>> is_schrikkel(2023)
    False
    >>> is_schrikkel(1900)
    False
    >>> is_schrikkel(2000)
    True
    """
    if ((y%4 == 0) and (y%100 != 0)) or (y%400 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    y = int(input('Geef een jaartal: '))
    schrikkeljaarbool = is_schrikkel(y)
    if schrikkeljaarbool==True:
        print(y, "is een schrikkeljaar")
    else:
        print(y, "is geen schrikkeljaar")
    