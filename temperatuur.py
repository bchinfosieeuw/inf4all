def get_positive_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Wat is de stapgrootte? "))
    while result <= 0:
        result = int(input("Wat is de stapgrootte? "))
    return result

def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.
    """
    new_temp = 0
    if old_type=='C' or old_type=='c':
        new_temp = round((old_temp*18 + 320) // 10)
        print("C |   F")
    else:
        new_temp = int((old_temp*10 - 320) // 18)
        print("F |   C")
    return new_temp

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
    mybool = False
    if old_temp > new_temp:
        mybool = True
    step_size = 0
    if mybool==False:
        step_size = get_positive_int()
        new_temp = convert_temperature(old_type, old_temp)
        print(new_temp)