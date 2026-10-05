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
    
    >>> convert_temperature('c', 0)
    32
    
    >>> convert_temperature('f', 0)
    -17
    
    >>> convert_temperature('C', 15)
    59
    """
    new_temp = 0
    if old_type=='C' or old_type=='c':
        new_temp = int((old_temp*18 + 320) // 10)
    else:
        new_temp = int((old_temp*10 - 320) // 18 + 1)
    return new_temp

def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.
    
    >>> print_table('C', 0, 20, 5)
      0 |  32
      5 |  41
     10 |  50
     15 |  59
     20 |  68
    
    >>> print_table('F', 0, 10, 2)
      0 | -17
      2 | -16
      4 | -15
      6 | -14
      8 | -13
     10 | -12
    
    >>> print_table('F', 0, 10, 3)
      0 | -17
      3 | -16
      6 | -14
      9 | -12
    """
    i = 0
    old_temp = begin_temp
    while end_temp-step_size+1 > begin_temp + (i-1)*step_size:
        new_temp = convert_temperature(old_type, old_temp)
        print(f"{old_temp:>3}", end='')
        print(' | ', end='')
        print(f"{new_temp:>3}", end='')
        print()
        old_temp += step_size
        i += 1

if __name__ == '__main__':
    old_type = input('Welke eenheid van temperatuur (C of F)? ')
    while old_type!='C' and old_type!='c' and old_type!='F' and old_type!='f':
        old_type = input('Welke eenheid van temperatuur (C of F)? ')
    old_temp = int(input('Wat is de begintemperatuur? '))
    new_temp = int(input('Wat is de eindtemperatuur? '))
    mybool = False
    if old_temp > new_temp:
        mybool = True
    step_size = get_positive_int()
    if old_type=='C' or old_type=='c':
        print("  C |   F")
    else :
        print("  F |   C")
    if mybool==False:
        print_table(old_type, old_temp, new_temp, step_size)