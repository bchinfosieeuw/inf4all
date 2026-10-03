def print_collatz(n: int) -> None:
    print(n)
    while n > 1:
        if (n+2)%2==0:
            n = n // 2
            print(n)
        else:
            n = n*3 + 1
            print(n)

def print_collatz(n: int) -> None:
    
    
print_collatz(3)