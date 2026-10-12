def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
    """
    return len(password) >= 8

def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.
    """

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """

def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.
    """
    if check_length(password) and check_letter(password) and
    check_number(password):
        return True
    else:
        return False

if __name__ == '__main__':
    passwordProposal = input('Geef een wachtwoord:')
    passwordValidity = check_password(passwordProposal)
    if passwordValidity==True:
        print('Het gegeven wachtwoord is valide.')
    else:
        print('Het gegeven wachtwoord is niet valide.')