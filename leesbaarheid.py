def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    
    """
    words = 1
    for c in text:
        if c==" ":
            words += 1
    sentences = 0
    for c in text:
        if c in ".!":
            sentences += 1
    letters = 0
    for c in text:
        if c.isalpha():
            letters += 1
    index = round(coleman_liau(words, sentences, letters))
    return index

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    """

if __name__ == '__main__':
    text = input('Text: ')
    index = calculate_grade(text)
    if index < 1:
        print('')