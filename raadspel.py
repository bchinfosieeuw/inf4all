import random

def get_positive_int() -> int:
    """
    Deze functie vereist een positieve integer.
    """
    result = int(input("Enter a positive int: "))
    while result <= 0:
        result = int(input("Enter a positive int: "))
    return result
    
def check_guess(guess: int, number: int) -> bool:
    """
    Check of de gok goed is. Als de gok niet goed is, return dan
    False en print of de gok te groot of te klein is.
    """
    mybool = False
    if guess > number:
        print("Je gok is te groot!")
    elif guess < number:
        print("Je gok is te klein!")
    else:
        print("Je hebt het getal goed geraden, gefeliciteerd!")
        mybool = True
    return mybool

def decide_number(level: int) -> int:
    """
    Kies een willekeurig getal tussen 1 en level.

    >>> decide_number(1)
    1
    >>> decide_number(100) <= 100
    True
    >>> 1 <= decide_number(2) <= 2
    True
    """
    a = 1
    b = level
    return random.randint(a, b)

if __name__ == '__main__':
    level = get_positive_int()
    randomgetal = decide_number(level)
    guess = get_positive_int()
    mybool = check_guess(gok, randomgetal)
    while mybool==False:
        if gok!=randomgetal:
            gok = get_positive_int()
        mybool = check_guess(gok, randomgetal)