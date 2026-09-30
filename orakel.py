def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties
    42, tweeenveertig, of tweeënveertig is.
    
    >>> check_answer()
    
    """

if __name__ == '__main__':
    answerUser = input('Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?')
    boolOracle = check_answer(answerUser)
    if boolOracle==True:
        print("Ja")
    else:
        print("Nee")