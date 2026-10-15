def add(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = 0
    if len(str(n))==2:
        n10 = int(str(n)[-2])
    m1 = int(str(m)[-1])
    m10 = 0
    if len(str(m))==2:
        m10 = int(str(m)[-2])
    mybool1 = False
    mybool10 = False
    if n1 + m1 >= 10:
        numOfCarries += 1
                    mybool1 = True
                    break
        if mybool10==False:
            for j10 in range (m):
                if n10 + m10 >= 10:
                    numOfCarries += 1
                    mybool10 = True
                    break
    return numOfCarries

def mul(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = 0
    if len(str(n))==2:
        n10 = int(str(n)[-2])
    m1 = int(str(m)[-1])
    m10 = 0
    if len(str(m))==2:
        m10 = int(str(m)[-2])
    mybool1A = False
    mybool10A = False
    mybool1B = False
    mybool10B = False
    for i in range (n):
        if mybool1A==False:
            for j1 in range (m):
                if n1 * m1 >= 10:
                    numOfCarries += 1
                    mybool1A = True
                    break
        if mybool10A==False:
            for j10 in range (m):
                if n1 * m10 >= 10:
                    numOfCarries += 1
                    mybool10A = True
                    break
        if mybool1B==False:
            for j1 in range (m):
                if n10 * m1 >= 10:
                    numOfCarries += 1
                    mybool1B = True
                    break
        if mybool10B==False:
            for j10 in range (m):
                if n10 * m10 >= 10:
                    numOfCarries += 1
                    mybool10B = True
                    break
    return numOfCarries
    
if __name__ == '__main__':
    N = int(input('N: '))
    M = int(input('M: '))
    numOfCarriesAdd = 0
    maxOfCarriesAdd = 0
    for n in range(N):
        for m in range(M):
            numOfCarriesAdd = add(n, m)
            if numOfCarriesAdd==1:
                maxOfCarriesAdd += 1
    numOfCarriesMul = 0
    maxOfCarriesMul = 0
    for n in range(N):
        for m in range(M):
            numOfCarriesMul = mul(n, m)
            if numOfCarriesMul==2:
                maxOfCarriesMul += 1
    numOfCarriesMul = mul(n, m)
    print(maxOfCarriesAdd)
    print(maxOfCarriesMul)