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
    count = 0
    diff = eind-begin
    for i in range(diff):
        
    
print(tel_schrikkeljaren(1800, 1808))