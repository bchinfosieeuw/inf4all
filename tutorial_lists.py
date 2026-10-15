"""
tutorial_lists.py

Kopieer elke functie uit de uitleg hiernaast naar dit bestand en vul daarna
de body in. Klik op de knop doctest om je werk te controleren.
"""


def make_list() -> list[int]:
    """
    >>> make_list()
    [1, 2, 3]
    """
    return [1, 2, 3]
    
    


def first_item(xs: list[int]) -> int:
    """
    >>> first_item([10, 20, 30])
    10
    >>> first_item([7])
    7
    """
    return xs[0]
    



def last_item(xs: list[int]) -> int:
    """
    >>> last_item([10, 20, 30])
    30
    >>> last_item([5])
    5
    """
    return xs[-1]



def first_two(xs: list[int]) -> list[int]:
    """
    >>> first_two([10, 20, 30, 40])
    [10, 20]
    >>> first_two([1, 2])
    [1, 2]
    """
    return xs[0:2]
    
    


def replace_first(xs: list[str], value: str) -> None:
    """
    >>> letters = ["x", "y", "z"]
    >>> replace_first(letters, "A")
    >>> letters
    ['A', 'y', 'z']
    """
    xs[0] = value
    
    


def add_last(xs: list[int], item: int) -> None:
    """
    >>> numbers = [1, 2]
    >>> add_last(numbers, 3)
    >>> numbers
    [1, 2, 3]
    """
    xs.append(item)
    
    


def add_at(xs: list[str], index: int, item: str) -> None:
    """
    >>> letters = ["a", "c"]
    >>> add_at(letters, 1, "b")
    >>> letters
    ['a', 'b', 'c']
    """
    xs.insert(index, item)
    
    


def remove_first(xs: list[int], value: int) -> None:
    """
    >>> numbers = [1, 2, 3, 2]
    >>> remove_first(numbers, 2)
    >>> numbers
    [1, 3, 2]
    """
    xs.remove(value)
    
    


def take_last(xs: list[int]) -> int:
    """
    >>> numbers = [1, 2, 3]
    >>> take_last(numbers)
    3
    >>> numbers
    [1, 2]
    """
    return xs.pop()


def combine(a: list[int], b: list[int]) -> list[int]:
    """
    >>> combine([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> combine([], [5])
    [5]
    """
    return a + b
    


def zeros(n: int) -> list[int]:
    """
    >>> zeros(3)
    [0, 0, 0]
    >>> zeros(0)
    []
    """
    return [0] * n
    
    


def has_value(xs: list[str], value: str) -> bool:
    """
    >>> has_value(["a", "b", "c"], "b")
    True
    >>> has_value(["a", "b", "c"], "z")
    False
    """
    return value in xs
    
    


def count_value(xs: list[int], value: int) -> int:
    """
    >>> count_value([1, 2, 2, 3], 2)
    2
    >>> count_value([1, 2, 3], 9)
    0
    """
    return xs.count(value)
    
    


def position(xs: list[str], value: str) -> int:
    """
    >>> position(["a", "b", "c"], "c")
    2
    >>> position(["a", "b", "c"], "z")
    -1
    """
    if value in xs:
        return xs.index(value)
    else:
        return -1
        
        


def total(xs: list[int]) -> int:
    """
    >>> total([1, 2, 3])
    6
    >>> total([])
    0
    """
    i = 0
    for number in xs:
        i += number
    return i



def biggest(xs: list[int]) -> int:
    """
    >>> biggest([3, 9, 2])
    9
    >>> biggest([-5, -2, -8])
    -2
    >>> biggest([7])
    7
    """
    i = xs[0]
    for number in range(len(xs)):
        if xs[number] > i:
            i = xs[number]
    return i



def positives(xs: list[int]) -> list[int]:
    """
    >>> positives([-2, 0, 5, 7, -1])
    [5, 7]
    >>> positives([-1, -2])
    []
    """
    result = []
    for item in xs:
        if item > 0:
            result.append(item)
    return result


def multiply_all(xs: list[int], factor: int) -> list[int]:
    """
    >>> multiply_all([1, 2, 3], 10)
    [10, 20, 30]
    >>> numbers = [1, 2]
    >>> multiply_all(numbers, 5)
    [5, 10]
    >>> numbers
    [1, 2]
    """
    mylist = []
    for index in xs:
        mylist.append(index * factor)
    return mylist
    
    


def is_sorted(xs: list[int]) -> bool:
    """
    >>> is_sorted([1, 2, 2, 5])
    True
    >>> is_sorted([1, 3, 2])
    False
    >>> is_sorted([])
    True
    """
    for index in range(len(xs) - 1):
        if xs[index] > xs[index + 1]:
            return False
    return True
    
    


def sorted_copy(xs: list[int]) -> list[int]:
    """
    >>> numbers = [3, 1, 2]
    >>> sorted_copy(numbers)
    [1, 2, 3]
    >>> numbers
    [3, 1, 2]
    """
    return sorted(xs)
    
    


def with_zero(xs: list[int]) -> list[int]:
    """
    >>> numbers = [1, 2]
    >>> with_zero(numbers)
    [1, 2, 0]
    >>> numbers
    [1, 2]
    """
    newlist = xs.copy()
    newlist.append(0)
    return newlist
    
    
