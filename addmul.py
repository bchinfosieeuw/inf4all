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
        
    r1 = int(str(h1) + str(h10))
    r2 = int(str(h2) + str(h20))
    r3 = int(str(h3) + str(h30))
    r4 = int(str(h4) + str(h40))
    
    
    s1 = int(str(r1)[-1])
    s10 = 0
    if len(str(r1))==2:
        s10 = int(str(r1)[-2])
    s2 = int(str(r2)[-1])
    s20 = 0
    if len(str(r2))==2:
        s20 = int(str(r2)[-2])
    s3 = int(str(r3)[-1])
    s30 = 0
    if len(str(r3))==2:
        s30 = int(str(r3)[-2])
    s4 = int(str(r4)[-1])
    s40 = 0
    if len(str(r4))==2:
        s40 = int(str(r4)[-2])
    
    
    if s10 + s2 + s3 >= 10:
        numOfCarries += 1
        if n20 + m30 + s4 + 1 >= 10:
            numOfCarries += 1
            if s40 + 1 >= 10:
                numOfCarries += 1
    elif n20 + m30 +s4 >= 10:
        numOfCarries += 1
    
    return numOfCarries
    
if __name__ == '__main__':
    N = 99#int(input('N: '))
    #M = int(input('M: '))
    numOfCarriesAdd = 0
    maxOfCarriesAdd = 0
    numOfCarriesMul = 0
    maxOfCarriesMul = 0
    maxOfCarriesAddremem = -1
    maxOfCarriesMulremem = -1
    for n in range(N+1):
        for m in range(N+1):
            numOfCarriesAdd = add(n, m)
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