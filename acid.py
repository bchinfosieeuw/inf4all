def is_acidic(ph: float) -> bool:
    """
    is_acidic(6.9)
    Het is een zuur
    
    is_acidic(8.0)
    Het is een base
    
    is_acidic(7.0)
    Het is een base
    """
    if ph < 7.0:
        print("Het is een zuur")
    else:
        print("Het is een base")

if __name__ == '__main__':
    ph = float(input('Geef een pH-waarde: '))
    zuurofbase = is_acidic(ph)