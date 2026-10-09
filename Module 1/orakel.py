def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties
    42, tweeenveertig, of tweeënveertig is.
    
    >>> check_answer('42')
    True
    
    >>> check_answer('tweeenveertig')
    True
    
    >>> check_answer('tweeënveertig')
    True
    
    >>> check_answer('41')
    False
    
    >>> check_answer('vijfenveertig')
    False
    """
    if (answer=='42' or answer=='tweeenveertig' or answer=='tweeënveertig'):
        return True
    else:
        return False

if __name__ == '__main__':
    question1 = 'Wat is het antwoord op de grote vraag van het leven, '
    question2 = 'het universum en alles daarbij?'
    question = question1 + question2
    answerUser = input(question)
    boolOracle = check_answer(answerUser)
    if boolOracle==True:
        print("Ja")
    else:
        print("Nee")