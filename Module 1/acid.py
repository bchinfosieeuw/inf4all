def is_acidic(ph: float) -> bool:
    """
    Bepaal aan de hand van de pH-waarde of de stof een zuur of base is.
    
    >>> is_acidic(6.9)
    True
    
    >>> is_acidic(8.0)
    False
    
    >>> is_acidic(7.0)
    False
    """
    if ph < 7.0:
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
    