from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
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
    length = 0
    i = 2
    maxlength = 0
    onder = 0
    mybool = True
    while i < N:
        if is_priem(i)==False:
            length += 1
            if maxlength < length:
                maxlength = length
            if mybool==True:
                mybool = False
                onder = i
        else:
            if maxlength <= length:
                length = 0
                mybool = True
        i += 1
    length = 0
    i = 2
    maxlength = 0
    boven = 0
    mybool = True
    while i < N:
        if is_priem(i)==True:
            length += 1
            if maxlength < length:
                maxlength = length
            if mybool==True:
                mybool = False
                boven = i
        else:
            if maxlength <= length:
                length = 0
                mybool = True
        i += 1
    return onder, boven-1
    
def print_boodschap(onder: int, boven: int) -> None:
    """
    Print de samenvatting op het scherm.
    
    >>> print_boodschap(9950, 9972)
    De langste reeks niet-priemgetallen onder de 10,000 begint op 9950 en
     eindigt bij 9972
    De reeks is 23 lang.
    
    >>> print_boodschap(90, 96)
    De langste reeks niet-priemgetallen onder de 10,000 begint op 90 en
     eindigt bij 96
    De reeks is 7 lang.
    
    >>> print_boodschap(0, 1)
    De langste reeks niet-priemgetallen onder de 10,000 begint op 0 en
     eindigt bij 1
    De reeks is 2 lang.
    """
    reekslengte = boven-onder+1
    print('De langste reeks niet-priemgetallen onder de 10,000 ', end="")
    print('begint op ', end="")
    print(onder, 'en eindigt bij', boven)
    print('De reeks is', reekslengte, 'lang.')
    
if __name__ == '__main__':
    onder = 0
    boven = 0
    (onder, boven) = zoek_langste_reeks(10000)
    print_boodschap(onder, boven)