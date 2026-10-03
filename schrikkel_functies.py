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

def tel_schrikkeljaren(begin: int, eind: int) -> int:
    """
    Tel het aantal schrikkeljaren tussen en inclusief begin en eind.
    
    >>> tel_schrikkeljaren(1800, 1804)
    1
    
    >>> tel_schrikkeljaren(1800, 1808)
    2
    
    >>> tel_schrikkeljaren(1804, 1812)
    3
    """
    count = 0
    diff = eind-begin
    for i in range(diff+1):
        if is_schrikkel(begin+i):
            count += 1
    return count

def nde_schrikkeljaar_vanaf(begin: int, n: int) -> int:
    """
    Geef het n-de schrikkeljaar vanaf in inclusief begin.
    
    >>> nde_schrikkeljaar_vanaf(1800, 1)
    1804
    
    >>> nde_schrikkeljaar_vanaf(1800, 2)
    1808
    
    >>> nde_schrikkeljaar_vanaf(1804, 2)
    1808
    """
    leapyear = 0
    plus1 = 1
    if is_schrikkel(begin):
        plus1 = 0
    for i in range(4*n+plus1):
        if is_schrikkel(begin+i):
            leapyear = begin+i
    return leapyear
