"""
tutorial_transformatie.py

Kopieer elke functie uit de uitleg hiernaast naar dit bestand en vul daarna
de body in. Klik op de knop doctest om je werk te controleren.
"""


def kopie(s: str) -> str:
    """
    >>> kopie("hallo")
    'hallo'
    >>> kopie("")
    ''
    """
    nieuwe_string = ""
    for teken in s:
        nieuwe_string += teken
    return nieuwe_string


def hoofdletters(s: str) -> str:
    """
    >>> hoofdletters("hallo")
    'HALLO'
    >>> hoofdletters("Dag 3!")
    'DAG 3!'
    """
    nieuwe_string = ""
    for teken in s:
        nieuwe_string += teken.upper()
    return nieuwe_string


def spaties_naar_streepjes(s: str) -> str:
    """
    >>> spaties_naar_streepjes("hallo daar")
    'hallo_daar'
    >>> spaties_naar_streepjes("een twee drie")
    'een_twee_drie'
    """
    nieuwe_string = ""
    for teken in s:
        if teken==" ":
            nieuwe_string += "_"
        else:
            nieuwe_string += teken
    return nieuwe_string



def verberg_klinkers(s: str) -> str:
    """
    >>> verberg_klinkers("python")
    'pyth*n'
    >>> verberg_klinkers("Amsterdam")
    '*mst*rd*m'
    """
    nieuwe_string = ""
    for teken in s:
        if teken.lower() in "aeiou":
            nieuwe_string += "*"
        else:
            nieuwe_string += teken
    return nieuwe_string
    


def l337sp34k(s: str) -> str:
    """
    >>> l337sp34k("leet")
    '1337'
    >>> l337sp34k("Hallo Toto!")
    'H4110 7070!'
    """
    nieuwe_string = ""
    for teken in s:
        if teken in "aA":
            nieuwe_string += "4"
        elif teken in "eE":
            nieuwe_string += "3"
        elif teken in "lL":
            nieuwe_string += "1"
        elif teken in "oO":
            nieuwe_string += "0"
        elif teken in "tT":
            nieuwe_string += "7"
        else:
            nieuwe_string += teken
    return nieuwe_string


def verberg_cijfers(s: str) -> str:
    """
    >>> verberg_cijfers("pincode 1234")
    'pincode ####'
    >>> verberg_cijfers("R2D2")
    'R#D#'
    """
    nieuwe_string = ""
    for teken in s:
        if teken.isdigit():
            nieuwe_string += "#"
        else:
            nieuwe_string += teken
    return nieuwe_string


def blackout(s: str) -> str:
    """
    >>> blackout("Geheim!")
    '######!'
    >>> blackout("R2D2 is 1 robot.")
    '#2#2 ## 1 #####.'
    """
    nieuwe_string = ""
    for teken in s:
        if teken.isalpha():
            nieuwe_string += "#"
        else:
            nieuwe_string += teken
    return nieuwe_string


def replace_char(s: str, c1: str, c2: str) -> str:
    """
    >>> replace_char("banaan", "a", "o")
    'bonoon'
    >>> replace_char("hallo daar", " ", "_")
    'hallo_daar'
    """
    nieuwe_string = ""
    for teken in s:
        if teken==c1:
            nieuwe_string += c2
        else:
            nieuwe_string += teken
    return nieuwe_string



def zonder_spaties(s: str) -> str:
    """
    >>> zonder_spaties("hallo daar")
    'hallodaar'
    >>> zonder_spaties(" a b c ")
    'abc'
    """
    nieuwe_string = ""
    for teken in s:
        if teken!=" ":
            nieuwe_string += teken
    return nieuwe_string



def verwijder_n(s: str) -> str:
    """
    >>> verwijder_n("banaan")
    'baaa'
    >>> verwijder_n("nu niet")
    'u iet'
    """
    nieuwe_string = ""
    for teken in s:
        if teken!="n":
            nieuwe_string += teken
    return nieuwe_string
    

def kopie_met_posities(s: str) -> str:
    """
    >>> kopie_met_posities("hallo")
    'hallo'
    >>> kopie_met_posities("")
    ''
    """
    nieuwe_string = ""
    for pos in range(len(s)):
        nieuwe_string += s[pos]
    return nieuwe_string
    



def laatste_letters(s: str) -> str:
    """
    >>> laatste_letters("hallo daar")
    'or'
    >>> laatste_letters("een twee drie")
    'nee'
    """
    nieuwe_string = ""
    for pos in range(len(s)):
        if pos == len(s) - 1 or s[pos + 1] == " ":
            nieuwe_string += s[pos]
    return nieuwe_string



def verwijder_n_eind(s: str) -> str:
    """
    >>> verwijder_n_eind("lopen en fietsen")
    'lope e fietse'
    >>> verwijder_n_eind("banaan, nu even.")
    'banaa, nu eve.'
    """
    nieuwe_string = ""
    for pos in range(len(s)):
        if not(pos == len(s) - 1 or not s[pos + 1].isalpha()):
            nieuwe_string += s[pos]
        elif s[pos] in ".,":
            nieuwe_string += s[pos]
        elif s[pos] not in "n":
            nieuwe_string += s[pos]
    return nieuwe_string


def eerste_letters(s: str) -> str:
    """
    >>> eerste_letters("hallo daar")
    'hd'
    >>> eerste_letters("een twee drie")
    'etd'
    """
    nieuwe_string = ""
    for pos in range(len(s)):
        if pos == 0 or s[pos - 1] == " ":
            nieuwe_string += s[pos]
    return nieuwe_string


def verwijder_n_begin(s: str) -> str:
    """
    >>> verwijder_n_begin("nu niet")
    'u iet'
    >>> verwijder_n_begin("banaan,nee")
    'banaan,ee'
    """
    nieuwe_string = ""
    for pos in range(len(s)):
        if not(pos == 0 or not s[pos - 1].isalpha()):
            nieuwe_string += s[pos]
        elif s[pos] not in "n":
            nieuwe_string += s[pos]
    return nieuwe_string
