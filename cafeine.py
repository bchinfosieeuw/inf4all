def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
    """
    return 

if __name__ == '__main__':
    coffee = int(input('Hoeveel koppen koffie? '))
    tea = int(input('Hoeveel koppen thee? '))
    aantalenergiedrankjes = int(input('Hoeveel energiedrankjes? '))
    aantalglazencola = int(input('Hoeveel glazen cola? '))
    hoeveelheidcafeine = calculate_cafeine(coffee, tea, aantalenergiedrankjes, aantalglazencola)
    print(hoeveelheidcafeine)