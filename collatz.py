def print_collatz(n: int) -> None:
    """
    """
    print(n)
    while n > 1:
        if (n+2)%2==0:
            n = n // 2
            print(n)
        else:
            n = n*3 + 1
            print(n)

def collatz_length(n: int) -> None:
    count = 1
    while n > 1:
        if (n+2)%2==0:
            n = n // 2
            count += 1
        else:
            n = n*3 + 1
            count += 1
    print(count)
