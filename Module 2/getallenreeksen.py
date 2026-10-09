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
    for i in range(1, 16, 1):
        print(j)
        j += i*2-1

def reeks4() -> None:
    """
    >>> reeks4()
    5
    4
    3
    2
    1
    0
    -1
    -2
    -3
    """
    for i in range(5, -4, -1):
        print(i)

def reeks5() -> None:
    """
    >>> reeks5()
    1
    3
    9
    27
    81
    243
    729
    """
    i = 1
    while i < 1000:
        print(i)
        i = i*3

def reeks6() -> None:
    """
    >>> reeks6()
    1000
    100
    10
    1
    0
    0
    0
    0
    0
    0
    """
    i = 1000
    j = 0
    while j < 10:
        print(i)
        i = i // 10
        j += 1

def reeks7() -> None:
    """
    >>> reeks7()
    1
    2
    *
    4
    5
    *
    7
    8
    *
    10
    """
    mystr = ""
    for i in range(1, 11, 1):
        mystr = str(i)
        if (i+3)%3==0:
            mystr = "*"
        print(mystr)

def reeks8() -> None:
    """
    >>> reeks8()
    1
    2
    #
    8
    16
    #
    64
    128
    #
    512
    """
    mystr = ""
    i = 1
    j = 0
    while j < 10:
        mystr = str(i)
        if (j+3)%3==2:
            mystr = "#"
        print(mystr)
        i = i * 2
        j += 1
