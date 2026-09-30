def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
    """
    return 

if __name__ == '__main__':
    coffee = int(input('Hoeveel koppen koffie? '))
    tea = int(input('Hoeveel koppen thee? '))
    energy = int(input('Hoeveel energiedrankjes? '))
    cola = int(input('Hoeveel glazen cola? '))
    quantityofcafein = calculate_cafeine(coffee, tea, energy, cola)
    print(quantityofcafein)