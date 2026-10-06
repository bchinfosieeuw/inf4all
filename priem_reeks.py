from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
    """
    """
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
    return maxlength
    
def print_boodschap() -> None:
    print('')
    print('')
    
if __name__ == '__main__':
    maxlength = zoek_langste_reeks(100)
    print_boodschap(maxlength)