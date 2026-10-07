from priem_getal import is_priem

def apply_goldbach(N: int) -> int:
    """
    Comment
    
    >>> apply_goldbach(1000)
    
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
    apply_goldbach(1000)