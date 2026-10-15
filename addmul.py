def add(n: int, m: int) -> int:
    i = 0
    numOfCarries = 0
    for i in range (n):
        for j in range (m):
    return numOfCarries
    
if __name__ == '__main__':
    n = int(input('n:'))
    m = int(input('m:'))
    print(add(n, m))