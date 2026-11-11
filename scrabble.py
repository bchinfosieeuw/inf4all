POINTS = [1, 3, 3,  2, 1, 4, 2, 4, 1, 8, 5, 1,  3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def compute_score(word: str) -> int:
    """
    Bereken en return de score voor het woord.
    Gebruikt for om door het ingetypte woord te loopen waarbij elke letter 
    afzonderlijk naar compute_letter_score wordt gestuurd om het aantal punten 
    te bepalen van deze letter. Speciale karakters en getallen worden genegeerd
    waarbij er geen score voor deze tekens wordt opgeteld.
    
    >>> compute_letter_score("a")
    1
    """
    wordscore = 0
    for i in range(len(word)):
        if word[i] not in ".,;!? ":
            wordscore += compute_letter_score(word[i].lower())
    return wordscore

def compute_letter_score(letter: str) -> int:
    """
    Bereken en return de score voor één enkele letter.
    In het alfabet zitten alleen kleine letters, en compute_letter_score krijgt 
    alleen kleine letters ingevoerd. De for loop herhaalt het aantal keer dat 
    er letters zijn in dit alfabet. De positie van de ingevoerde letter in het 
    alfabet wordt bepaald, waarna het aantal punten volgens de global POINTS 
    aan de letterscore wordt toegekend.
    
    >>> compute_letter_score("A")
    1
    
    >>> compute_letter_score("a")
    1
    
    >>> compute_letter_score("z")
    10
    
    >>> compute_letter_score(",")
    0
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letterscore = 0
    for i in range(len(alphabet)):
        if letter==alphabet[i]:
            letterscore = POINTS[i]
    return letterscore

if __name__ == '__main__':
    word1 = input("Woord van speler 1: ")
    word2 = input("Woord van speler 2: ")
    score1 = compute_score(word1)
    score2 = compute_score(word2)
    print("Speler 1: ", end="")
    print(word1)
    print("Speler 2: ", end="")
    print(word2)
    if score1 > score2:
        print("Speler 1 wint!")
    elif score1 < score2:
        print("Speler 2 wint!")
    else:
        print("Gelijkspel!")