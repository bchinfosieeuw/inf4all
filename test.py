python3 -m doctest -v is_even.py
"""Comment"""
#Comment
print(round(7.8))
print(int(7.8))
print(f"Hierbij de som van 1 en 1: {1+1}")
letter = 'a'
print(f"{letter:10}")
print(f"{letter:>10}")
letter = 'bb'
print(f"{letter:10}")
print(f"{letter:>10}")
print('\"', end="")
print('Zon Maa Din Woe Don Vri Zat', end="")
print('\"')
range(10) geeft de getallen van 0 tot 10, dus eindigt bij 9
range(1, 10) geeft de getallen 1 tot 10
range(-2, 9, 2) feeft de getallen van -2 tot 9, in stappen van 2
.upper() geeft een nieuwe string met hoofdletters
.lower() geeft een nieuwe string met kleine letters
.capitalize() geeft een nieuwe string, eerste letter wordt hoofdletter, rest kleine letters
.isupper() bepaalt of de string alleen hoofdletters heeft
.isalpha() bepaalt of de string alleen letters heeft
.isdigit() bepaalt of de string alleen cijfers heeft
formula = input()#2 + 3
x, y, z = formula.split(" ")
def calculate_grade(time: str) -> str | None:
    """
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    9
    """
    if ...:
        return time
    return None
from priem_getal import is_priem
def zoek_langste_reeks(N: int) -> tuple[int, int]:
    return minonder, minboven-1
import random
random.randint(a, b)
def rotate(lst: list[object]) -> None: