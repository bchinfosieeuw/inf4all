from priem_getal import is_priem

def apply_goldbach(N: int) -> int:
    """
    Check of alle even getallen tot en met N 
    
    >>> apply_goldbach(10)
    4 = 2 = 2
    6 = 3 + 3
    8 = 3 + 5
    10 = 3 + 7
    
    >>> apply_goldbach(5)
    4 = 2 = 2
    
    >>> apply_goldbach(16)
    4 = 2 = 2
    6 = 3 + 3
    8 = 3 + 5
    10 = 3 + 7
    12 = 5 + 7
    14 = 3 + 11
    16 = 3 + 13
    """
    i1 = 0
    for i in range(N+1):
        if (i+2)%2==0:
            for p in range(N+1):
                if is_priem(p):
                    i1 = i - p
                    if is_priem(i1):
                        print(i, '=', p, '+', i1)
                        break
if __name__ == '__main__':
    apply_goldbach(16)