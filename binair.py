def convert(bit1: int, bit2: int, bit3: int, bit4: int) -> int:
    """
    Zet het getal dat gerepresenteerd wordt door bit1 t/m bit 4
    om in decimale representatie.
    
    >>>
    """
    return bit1*4+bit2*3+bit3*2+bit4^1

if __name__ == '__main__':
    bit1 = int(input('Geef 0 of 1 als invoer als 1e van 4 bits'))
    bit2 = int(input('Geef 0 of 1 als invoer als 2e van 4 bits'))
    bit3 = int(input('Geef 0 of 1 als invoer als 3e van 4 bits'))
    bit4 = int(input('Geef 0 of 1 als invoer als 4e van 4 bits'))
    decimaalgetal = convert(bit1, bit2, bit3, bit4)
    print(decimaalgetal)