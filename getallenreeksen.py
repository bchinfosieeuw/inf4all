def reeks1() -> None:
    """
    >>> reeks1()
    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    """
    for i in range(0, 20, 2):
        print(i)
        
def reeks2() -> None:
    """
    >>> reeks2()
    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
    23
    """
    for i in range(1, 25, 2):
        print(i)

def reeks3() -> None:
    """
    >>> reeks3()
    1
    2
    5
    10
    17
    26
    37
    50
    65
    82
    101
    122
    145
    170
    197
    """
    j = 1
    for i in range(1, 100, 1):
        print(j)
        j += i*2-1

def reeks1() -> None:
    """
    >>> reeks1()
    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    """
    for i in range(0, 20, 2):
        print(i)
        
reeks3()