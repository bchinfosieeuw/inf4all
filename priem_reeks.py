from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
    """
    """
    length = 0
    i = 2
    maxlength = 0
    onder = 0
    boven = 0
    while i < N:
        if is_priem(i)==False:
            length += 1
            if maxlength < length:
                maxlength = length
        else:
            length = 0
            onder = i
        i += 1
    boven = onder + 
    return onder, boven
    
def print_boodschap(maxlength: int) -> None:
    print('De langste reeks niet-priemgetallen onder de 100 begint op 90 en eindigt bij 96')
    print('De reeks is', maxlength, 'lang.')
    
if __name__ == '__main__':
    maxlength = zoek_langste_reeks(100)
    print_boodschap(maxlength)