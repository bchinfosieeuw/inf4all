def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.
    
    >>> check_input('ATGC')
    
    
    >>> check_input('ATGC')
    
    
    >>> check_input('ATGC')
    
    """
    for char in dna:
        if char not in "agctAGCT":
            return False
    return True

def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).
    """
    result = ""
    for char in dna:
        if char.upper()=="A":
            result += "U"
        elif char.upper()=="G":
            result += "C"
        elif char.upper()=="C":
            result += "G"
        elif char.upper()=="T":
            result += "A"
    return result

if __name__ == '__main__':
    s = input('DNA: ')
    if check_input(s)==True:
        print('RNA:', transcribe_dna_to_rna(s))
    else:
        print('That is not a valid DNA string')