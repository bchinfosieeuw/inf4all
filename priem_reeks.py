from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple[int, int]:
    """
    Bepaal de ondergrens en bovengrens van de reeks niet-priemgetallen tot aan
     gegeven getal N.
    
    >>> zoek_langste_reeks(100)
    (90, 96)
    
    >>> zoek_langste_reeks(10000)
    (9552, 9586)
    
    >>> zoek_langste_reeks(20)
    (8, 1)
    """
    length = 0
    i = 1
    maxlength = 0
    onder = 0
    minonder = 0
    minboven = 0
    while i < N:
        if is_priem(i)==False:
            j = i+1
            onder = i
            while j < N:
                if is_priem(j)==True:
                    boven = j-1
                    break
                j += 1
            length = boven-onder
        i += 1
        if length > maxlength:
            maxlength = length+1
            minonder = onder
    minboven = minonder + maxlength
    return minonder, minboven-1
    
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
    (onder, boven) = zoek_langste_reeks(10000)
    print_boodschap(onder, boven)