def add(n: int, m: int) -> int:
    numOfCarries = 0
    
    for i in range (n):
        for j in range (m):
    return numOfCarries

def mul(n: int, m: int) -> int:
    numOfCarries = 0
    for i in range (n):
        for j in range (m):
    return numOfCarries
    
if __name__ == '__main__':
    n = int(input('n:'))
    m = int(input('m:'))
    numOfCarriesAdd = add(n, m)
    numOfCarriesMul = mul(n, m)
    print(numOfCarriesAdd)
    print(numOfCarriesMul)