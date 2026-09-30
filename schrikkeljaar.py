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
    ph = float(input('Geef een pH-waarde: '))
    zuurofbase = is_acidic(ph)
    if zuurofbase==True:
        print("Het is een zuur")
    else:
        print("Het is een base")
    