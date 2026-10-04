import random

def get_positive_int_feedback() -> int:
    """
    Deze functie vereist een positieve integer.
    
    >>> get_positive_int_feedback() > 0
    True
    
    >>> get_positive_int_feedback() < 0
    False
    
    >>> get_positive_int_feedback() == 0
    False
    """
    result = int(input("Gok: "))
    while result <= 0:
        result = int(input("Gok: "))
    return result
    
def check_guess(guess: int, number: int) -> bool:
    """
    Check of de gok goed is. Als de gok niet goed is, return dan
    False en print of de gok te groot of te klein is.
    
    >>> check_guess(4, 4)
    True
    
    >>> check_guess(10, 5)
    False
    
    >>> check_guess(5, 10)
    False
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
    level = int(input("Level: "))
    while level <= 0:
        level = int(input("Level: "))
    randomgetal = decide_number(level)
    guess = get_positive_int_feedback()
    mybool = check_guess(guess, randomgetal)
    while mybool==False:
        if guess!=randomgetal:
            guess = get_positive_int_feedback()
        mybool = check_guess(guess, randomgetal)