from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
    """
    Bepaal de ondergrens en bovengrens van de reeks niet-priemgetallen tot aan gegeven getal N.
    
    >>> zoek_langste_reeks(100)
    (90, 96)
    
    >>> zoek_langste_reeks(10000)
    (9950, 9984)
    
    >>> zoek_langste_reeks(3)
    (0, -1)
    """
    length = 0
    i = 2
    maxlengthA = 0
    onder = 0
    mybool = True
    while i < N:
        if is_priem(i)==False:
            length += 1
            if maxlengthA < length:
                maxlengthA = length
            if mybool==True:
                mybool = False
                onder = i
        else:
            if maxlengthA <= length:
                length = 0
                mybool = True
        i += 1
    length = 0
    i = 2
    maxlengthB = 0
    boven = 0
    mybool = True
    while i < N:
        if is_priem(i)==True:
            length += 1
            if maxlengthB < length:
                maxlengthB = length
            if mybool==True:
                mybool = False
                boven = i
        else:
            if maxlengthB <= length:
                length = 0
                mybool = True
        i += 1
    return onder, boven-1+(maxlengthB-maxlengthA)
    
def print_boodschap(onder: int, boven: int) -> None:
    """
    Print de samenvatting op het scherm.
    
    >>> print_boodschap(9950, 9984)
    De langste reeks niet-priemgetallen onder de 10,000 begint op 9950 en eindigt bij 9984
    De reeks is 35 lang.
    
    >>> print_boodschap(90, 96)
    De langste reeks niet-priemgetallen onder de 10,000 begint op 90 en eindigt bij 96
    De reeks is 7 lang.
    
    >>> print_boodschap(2, 3)
    De langste reeks niet-priemgetallen onder de 10,000 begint op 2 en eindigt bij 3
    De reeks is 2 lang.
    """
    reekslengte = boven-onder+1
    if onder==0 and boven==-1:
        onder = 'GEEN'
        boven = 'GEEN'
        reekslengte = 0
    print('De langste reeks niet-priemgetallen onder de 10,000 begint op', onder, 'en eindigt bij', boven)
    print('De reeks is', reekslengte, 'lang.')
    
if __name__ == '__main__':
    (onder, boven) = zoek_langste_reeks(10000)
    print_boodschap(onder, boven)