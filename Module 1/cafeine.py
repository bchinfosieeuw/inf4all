def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
    drankjes van het type koffie, thee, energie, en cola.
    
    >>> calculate_cafeine(2, 1, 0, 0)
    225
    
    >>> calculate_cafeine(2, 0, 2, 0)
    340
    
    >>> calculate_cafeine(0, 0, 0, 1)
    40
    
    >>> calculate_cafeine(5, 0, 0, 0)
    450
    """
    return coffee*90+tea*45+energy*80+cola*40

if __name__ == '__main__':
    coffee = int(input('Hoeveel koppen koffie? '))
    tea = int(input('Hoeveel koppen thee? '))
    energy = int(input('Hoeveel energiedrankjes? '))
    cola = int(input('Hoeveel glazen cola? '))
    quantityofcafeine = calculate_cafeine(coffee, tea, energy, cola)
    print('Je krijgt', quantityofcafeine, 'mg cafeïne binnen.')