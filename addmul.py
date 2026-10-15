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
    if n1 + m1 >= 10:
        numOfCarries += 1
        if n10 + m10 + 1 >= 10:
            numOfCarries += 1
    elif n10 + m10 >= 10:
        numOfCarries += 1
    #print(numOfCarries)
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
    
    k1 = n1 * m1
    k2 = n1 * m10
    k3 = n10 * m1
    k4 = n10 * m10
    
    h1 = int(str(k1)[-1])
    h10 = 0
    if len(str(k1))==2:
        h10 = int(str(k1)[-2])
    h2 = int(str(k2)[-1])
    h20 = 0
    if len(str(k2))==2:
        h20 = int(str(k2)[-2])
    h3 = int(str(k3)[-1])
    h30 = 0
    if len(str(k3))==2:
        h30 = int(str(k3)[-2])
    h4 = int(str(k4)[-1])
    h40 = 0
    if len(str(k4))==2:
        h40 = int(str(k4)[-2])
    
    if h1 + h2 + h3 + h4 >= 10:
        numOfCarries += 1
        if h10 + h20 + h30 + h40 + 1 >= 10:
            numOfCarries += 1
    elif h10 + h20 + h30 + h40 >= 10:
        numOfCarries += 1
    return numOfCarries
    
if __name__ == '__main__':
    N = int(input('N: '))
    #M = int(input('M: '))
    numOfCarriesAdd = 0
    maxOfCarriesAdd = 0
    numOfCarriesMul = 0
    maxOfCarriesMul = 0
    maxOfCarriesAddremem = -1
    maxOfCarriesMulremem = -1
    for n in range(N+1):
        for m in range(n+1):
            numOfCarriesAdd = add(n, m+n)
            numOfCarriesMul = mul(n, m)
            if numOfCarriesAdd==1:# and maxOfCarriesAdd > maxOfCarriesAddremem:
                maxOfCarriesAdd += 1
                #maxOfCarriesAddremem = maxOfCarriesAdd
    #for n in range(N+1):
        #for m in range(M+1):
                if numOfCarriesMul==2:# and maxOfCarriesMul > maxOfCarriesMulremem:
                    maxOfCarriesMul += 1
                    #maxOfCarriesMulremem = maxOfCarriesMul
                    #print('n:', n)
                    #print('m:', m)
    print(maxOfCarriesAdd)
    print(maxOfCarriesMul)