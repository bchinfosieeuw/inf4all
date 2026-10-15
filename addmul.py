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
    h1 = int(str(k1)[-1])
    h10 = 0
    if len(str(k1))==2:
        h10 = int(str(k1)[-2])
    
    
    numOfCarries += add(k1, k2*10)
    numOfCarries += add(k3*10, k4*100)
    numOfCarries += add((k1+k2*10)//10, (k3*10+k4*100)//100)
    
    
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