from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple[int, int]:
    """
    Bepaal de ondergrens en bovengrens van de reeks niet-priemgetallen tot aan
     gegeven getal N.
    
    >>> zoek_langste_reeks(100)
    (90, 96)
    
    >>> zoek_langste_reeks(10000)
    (9950, 9972)
    
    >>> zoek_langste_reeks(3)
    (0, 1)
    """
    i = 2
    j = 0
    length = 0
    maxlength = 0
    onder = 0
    maxonder = 0
    mybool = True
    while i < N+1:
        if is_priem(i)==True:
            while is_priem(i+1+j)==False:
                onder += 1
                j += 1
            j = 0
        i += 1
    maxonder = onder
    i = 2
    length = 0
    maxlength = 0
    boven = 0
    maxboven = 0
    mybool = True
    while i < N:
        if is_priem(i)==True and is_priem(i+1)==False:
            length += 1
            if maxlength <= length:
                maxlength = length
            if mybool==True:
                mybool = False
                boven = i
        else:
            if maxlength <= length:
                length = 0
                mybool = True
                if maxboven < boven:
                    maxboven = boven
        i += 1
    return maxonder, maxboven-1
    
def print_boodschap(onder: int, boven: int) -> None:
    """
    Print de samenvatting op het scherm.
    """
    reekslengte = boven-onder+1
    print('De langste reeks niet-priemgetallen onder de 10,000 ', end="")
    print('begint op ', end="")
    print(onder, 'en eindigt bij', boven)
    print('De reeks is', reekslengte, 'lang.')
    
if __name__ == '__main__':
    onder = 0
    boven = 0
    (onder, boven) = zoek_langste_reeks(20)
    print_boodschap(onder, boven)
    (onder, boven) = zoek_langste_reeks(100)
    print_boodschap(onder, boven)
    (onder, boven) = zoek_langste_reeks(10000)
    print_boodschap(onder, boven)