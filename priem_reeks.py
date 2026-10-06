from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
    """
    Bepaal de ondergrens en bovengrens van de langste reeks niet-priemgetallen tot aan gegeven getal N.
    
    >>> zoek_langste_reeks(100)
    (90, 96)
    
    >>> zoek_langste_reeks(10000)
    (9950, 9984)
    
    >>> zoek_langste_reeks(3)
    (0, -1)
    """
    onder = 0
    boven = 0
    mybool = True
    onderremem = 0
    for i in range(N):
        if is_priem(i)==True and is_priem(i+1)==True:
            onder = i+1
        if is_priem(i)==True and is_priem(i+1)==False:
            
    return onder, boven
    
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
    (onder, boven) = zoek_langste_reeks(100)
    """diff(9552, 9586)==34"""
    print(onder, boven)
    """print_boodschap(onder, boven)"""