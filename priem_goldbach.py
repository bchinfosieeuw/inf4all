from priem_getal import is_priem

def apply_goldbach(N: int) -> None:
    """
    Geef een lijst van alle even getallen (groter dan 2) tot en met N als som
     van 2 priemgetallen.
    """
    q = 0
    for i in range(2, N+1):
        if (i+2)%2==0:
            for p in range(N+1):
                if is_priem(p)==True:
                    q = i - p
                    if is_priem(q)==True:
                        print(i, '=', p, '+', q)
                        break
                    elif is_priem(p)==False:
                        print('Het getal', i, end="")
                        print('is niet te schrijven als', end="")
                        print('som van 2 priemgetallen.')
                        
if __name__ == '__main__':
    apply_goldbach(1000)