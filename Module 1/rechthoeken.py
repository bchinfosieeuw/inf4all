def is_same_rectangle(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of de lengtes van de zijdes gelijk zijn
    
    >>> is_same_rectangle(1, 1, 2, 2)
    False
    
    >>> is_same_rectangle(1, 2, 1, 2)
    True
    
    >>> is_same_rectangle(1, 2, 3, 2)
    False
    """
    if ax_length==bx_length and ay_length==by_length:
        return True
    else:
        return False

def is_same_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of beide rechthoeken hetzelfde vierkant zijn
    
    >>> is_same_square(3, 3, 3, 3)
    True
    
    >>> is_same_square(1, 2, 1, 2)
    False
    
    >>> is_same_square(1, 2, 3, 2)
    False
    """
    if ax_length==ay_length==bx_length==by_length:
        return True
    else:
        return False

def calculate_length(c1: int, c2: int) -> int:
    """
    Berekent de lengte van een zijde op basis van twee coördinaten
    
    >>> calculate_length(6, 3)
    3
    
    >>> calculate_length(3, 6)
    3
    
    >>> calculate_length(0, 8)
    8
    """
    return abs(c1-c2)

if __name__ == '__main__':
    Ax1 = int(input('Geef de x1 van A: '))
    Ax2 = int(input('Geef de x2 van A: '))
    Ay1 = int(input('Geef de y1 van A: '))
    Ay2 = int(input('Geef de y2 van A: '))
    Bx1 = int(input('Geef de x1 van B: '))
    Bx2 = int(input('Geef de x2 van B: '))
    By1 = int(input('Geef de y1 van B: '))
    By2 = int(input('Geef de y2 van B: '))
    Axlength = calculate_length(Ax1, Ax2)
    Aylength = calculate_length(Ay1, Ay2)
    Bxlength = calculate_length(Bx1, Bx2)
    Bylength = calculate_length(By1, By2)
    if is_same_rectangle(Axlength, Aylength, Bxlength, Bylength)==True:
        print('De rechthoeken zijn gelijk!')
        if is_same_square(Axlength, Aylength, Bxlength, Bylength)==True:
            print('En ze zijn ook nog vierkant!')
    else:
        print('Er is niks aan :(')