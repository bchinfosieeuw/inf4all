def get_positive_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Enter a positive int: "))
    while result <= 0:
        result = int(input("Enter a positive int: "))
    return result

def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.
    """

def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.
    """

if __name__ == '__main__':
    old_type = input('Welke eenheid van temperatuur (C of F)? ')
    while old_type!='C' and old_type!='c' and old_type!='F' and old_type!='f':
        old_type = input('Welke eenheid van temperatuur (C of F)? ')
    old_temp = int(input('Wat is de begintemperatuur? '))
    new_temp = int(input('Wat is de eindtemperatuur? '))
    mybool = false
    print("F |   C")
    if old_temp <= new_temp:
        mybool = true
    step_size = 
    if mybool==false
        get_positive_int()