def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    
    >>> hoeveelheid_water(1)
    12
    
    >>> hoeveelheid_water(10)
    120
    
    >>> hoeveelheid_water(137)
    1644
    """
    return minuten*12

if __name__ == '__main__':
    doucheminuten = int(input('Hoeveel minuten douche je? '))
    aantalflesjeswater = hoeveelheid_water(doucheminuten)
    print(aantalflesjeswater)