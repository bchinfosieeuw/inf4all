def is_acidic(ph: float) -> bool:
    """
    is_acidic(6.0)
        
    """
    if ph < 7.0:
        print("Het is een zuur")
    else:
        print("Het is een base")

if __name__ == '__main__':
    ph = float(input('Geef een pH-waarde: '))
    zuurofbase = is_acidic(ph)