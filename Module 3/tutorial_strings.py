"""
tutorial_strings.py

Kopieer elke functie uit de uitleg hiernaast naar dit bestand en vul daarna
de body in. Klik op de knop doctest om je werk te controleren.
"""


def greet() -> str:
    """
    >>> greet()
    'Hello'
    """
    return 'Hello'


def first_char(s: str) -> str:
    """
    >>> first_char("Python")
    'P'
    >>> first_char("abc")
    'a'
    """
    return s[0]


def last_char(s: str) -> str:
    """
    >>> last_char("Python")
    'n'
    >>> last_char("code")
    'e'
    """
    return s[-1]


def excited(word: str) -> str:
    """
    >>> excited("Hi")
    'Hi!!!'
    >>> excited("You")
    'You!!!'
    """
    return word + '!' * 3


def double_and_space(a: str, b: str) -> str:
    """
    >>> double_and_space("go", "team")
    'gogo teamteam'
    """
    return a * 2 + ' ' + b * 2


def part_of_python(x: str) -> bool:
    """
    >>> part_of_python('py')
    True
    >>> part_of_python('n')
    True
    >>> part_of_python('java')
    False
    """
    return x in 'python'


def has_o(x: str) -> bool:
    """
    >>> has_o("dog")
    True
    >>> has_o("cat")
    False
    """
    for char in x:
        if char=='o':
            return True
    return False


def has_no_o(x: str) -> bool:
    """
    >>> has_no_o("cat")
    True
    >>> has_no_o("dog")
    False
    """
    for char in x:
        if char=='o':
            return False
    return True


def where_o_at(text: str) -> int:
    """
    >>> where_o_at("Python")
    4
    >>> where_o_at("abc")
    -1
    """
    for index in range(len(text)):
        if text[index] == 'o':
            return index
    return -1


def shout(s: str) -> str:
    """
    >>> shout("hello")
    'HELLO!'
    """
    return s.upper() + '!'


def quiet(s: str) -> str:
    """
    >>> quiet("LOUD")
    'loud...'
    """
    return s.lower() + '...'


def count_vowels(s: str) -> int:
    """
    >>> count_vowels("education")
    5
    >>> count_vowels("Python")
    1
    >>> count_vowels("RODENT!")
    2
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
