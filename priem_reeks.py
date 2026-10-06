from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
    """
    """
    length = 0
    i = 2
    maxlength = 0
    onder = 0
    boven = 0
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
    while i < N:
        if is_priem(i)==False:
            length += 1
            if maxlength < length:
                maxlength = length
        else:
            length = 0
        i += 1
    boven = onder + maxlength - 1
    return onder, boven
    
def print_boodschap(onder: int, boven: int) -> None:
    """
    Print de samenvatting op het scherm.
    
    >>> print_boodschap(90, 96)
    De langste reeks niet-priemgetallen onder de 100 begint op 9950 en eindigt bij 9984
    De reeks is 
    """
    print('De langste reeks niet-priemgetallen onder de 10,000 begint op', onder, 'en eindigt bij' ,boven)
    print('De reeks is', boven-onder+1, 'lang.')
    
if __name__ == '__main__':
    (onder, boven) = zoek_langste_reeks(10000)
    print_boodschap(onder, boven)