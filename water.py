def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    >>> hoeveelheid_water(1)
    12
    >>> hoeveelheid_water(10)
    12
    >>> hoeveelheid_water(1)
    12
    """

if __name__ == '__main__':
    //<vraag input, roep functie aan, en print resultaat
    doucheminuten = input('Hoeveel minuten douche je?')
    aantalflesjeswater = hoeveelheid_water(doucheminuten)
    print(aantalflesjeswater)