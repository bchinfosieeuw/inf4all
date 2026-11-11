POINTS = [1, 3, 3,  2, 1, 4, 2, 4, 1, 8, 5, 1,  3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def compute_score(word: str) -> int:
    """
    Bereken en return de score voor het woord.
    Gebruikt for om door het ingetypte woord te loopen waarbij elke letter 
    afzonderlijk naar compute_letter_score wordt gestuurd om het aantal punten 
    te bepalen van deze letter.
    """
    wordscore = 0
    for i in range(len(word)):
        wordscore += compute_letter_score(word[i].lower())
    return wordscore

def compute_letter_score(letter: str) -> int:
    """
    Bereken en return de score voor één enkele letter.
    In het alfabet zitten alleen kleine letters, en compute_letter_score krijgt 
    alleen kleine letters ingevoerd. De for loop 
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
    print(score1)
    print("Speler 2: ", end="")
    print(score2)
    #print("winner")