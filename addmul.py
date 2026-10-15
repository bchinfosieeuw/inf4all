def add(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = int(str(n)[-2])
    m1 = int(str(m)[-1])
    m10 = int(str(m)[-2])
    for i in range (n):
        for j in range (m):
            if n1 + m1 >
    return numOfCarries

def mul(n: int, m: int) -> int:
    numOfCarries = 0
    # i in range (n):
    #    for j in range (m):
    return numOfCarries
    
if __name__ == '__main__':
    n = int(input('n: '))
    m = int(input('m: '))
    numOfCarriesAdd = add(n, m)
    #numOfCarriesMul = mul(n, m)
    print(numOfCarriesAdd)
    #print(numOfCarriesMul)