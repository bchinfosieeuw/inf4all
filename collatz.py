def print_collatz(n: int) -> None:
    if (n+2)%2==0:
        n = n // 2
    else:
        n = n
    
print_collatz(5)