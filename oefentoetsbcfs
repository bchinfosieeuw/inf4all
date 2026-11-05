# Veel succes! Schrijf hieronder je functies
# en gebruik de knoppen voor checks!
def split_by_parity(ints: list[int]) -> list[list[int]]:
    """
    >>> split_by_parity([1, 2, 3, 4])
    [[2, 4], [1, 3]]
    """
    even = []
    oneven = []
    for i in range(len(ints)):
        if (i+2)%2==1:
            even.append(ints[i])
        else:
            oneven.append(ints[i])
    return [even, oneven]
    
def reading_level(s: str) -> float:
    """
    >>> reading_level("Mijn naam is Pim")
    9.75
    """
    vowels = "aeiou"
    space = " "
    numofvowels = 0
    numofnonvowels = 0
    numofalphabeticsigns = 0
    numofspaces = 0
    averagewordlength = 0.0
    level = 0.0
    for c in s:
        if c in vowels:
            numofvowels += 1
        elif c not in vowels and c not in space:
            numofnonvowels += 1
        if c in space:
            numofspaces += 1
        if c.isalpha():
            numofalphabeticsigns += 1
    #print(numofalphabeticsigns/(numofspaces+1))
    return (numofnonvowels-numofvowels)*(numofalphabeticsigns/(numofspaces+1))
    
    
if __name__ == '__main__':
    pass
    #reading_level("Mijn naam is Pim")
    #print(split_by_parity([1, 2, 3, 4]))