from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
    """
    """
    length = 0
    i = 0
    while i < N:
        if is_priem(N)==False:
            length += 1
        else:
            length = 0
        i += 1
    return length
    
if __name__ == '__main__':
    length = zoek_langste_reeks(100)
    print(length)