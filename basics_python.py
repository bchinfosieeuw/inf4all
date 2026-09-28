"""
basics_python.py

Bestudeer hoofdstuk 1 t/m 3 voordat je deze tutorial doorwerkt!!

Kopieer elke functie uit de uitleg hiernaast naar dit bestand en vul daarna
de body in. Klik op de knop doctest om je werk te controleren.
"""

import math

def kwadraat(a: int) -> int:
    """
    >>> kwadraat(6)
    36
    >>> kwadraat(2)
    4
    """
    return a * a
    
    
    
def derde_macht(a: int) -> int:
    """
    >>> derde_macht(2)
    8
    >>> derde_macht(5)
    125
    """
    return a * a * a
    


def avg3(a: float, b: float, c: float) -> float:
    """
    >>> avg3(1, 2, 3)
    2.0
    >>> avg3(10, 20, 60)
    30.0
    """
    return (a+b+c)/3
    



def celsius_to_fahrenheit(c: float) -> float:
    """
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(0)
    32.0
    """
    return c*9/5+32
    



def fahrenheit_to_celsius(f: float) -> float:
    """
    >>> fahrenheit_to_celsius(212)
    100.0
    >>> fahrenheit_to_celsius(32)
    0.0
    """
    return (f-32)*5/9
    



def is_divisible(a: int, b: int) -> bool:
    """
    >>> is_divisible(10, 5)
    True
    >>> is_divisible(10, 3)
    False
    """
    return a%b == 0
    



def is_leap_year(y: int) -> bool:
    """
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2023)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    return ((y%4 == 0) and (y%100 != 0)) or (y%400 == 0)
    



def pythagoras(a: float, b: float) -> float:
    """
    >>> pythagoras(3, 4)
    5.0
    >>> pythagoras(5, 12)
    13.0
    """
    return math.sqrt(a**2 + b**2)
    



def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """
    >>> is_valid_triangle(3, 4, 5)
    True
    >>> is_valid_triangle(1, 2, 10)
    False
    >>> is_valid_triangle(1, 1, 2)
    False
    """
    return (a+b > c) and (a+c > b) and (b+c > a)
    



def solve_quadratic(a: float, b: float, c: float) -> tuple:
    """
    >>> solve_quadratic(1, -3, 2)
    (2.0, 1.0)
    >>> solve_quadratic(1, 0, -4)
    (2.0, -2.0)
    """
    d = b * b - 4 * a * c
    solution1 = (-b+math.sqrt(d))/(2*a)
    solution2 = (-b-math.sqrt(d))/(2*a)
    return (solution1, solution2)