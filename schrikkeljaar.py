def is_leap_year(y: int) -> bool:
    """
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2023)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    if ((y%4 == 0) and (y%100 != 0)) or (y%400 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    y = int(input('Geef een jaartal: '))
    schrikkeljaarbool = is_leap_year(y)
    if schrikkeljaarbool==True:
        print(y, "is een schrikkeljaar")
    else:
        print(y, "is een schrikkeljaar")
    