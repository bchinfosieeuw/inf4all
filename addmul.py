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
    print(numOfCarries)
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
    
    if k1 + k1 >= 10:
        numOfCarries += 1
    if n1 + m10 >= 10:
        numOfCarries += 1
    if n10 + m1 >= 10:
        numOfCarries += 1
    if n10 + m10 >= 10:
        numOfCarries += 1
    return numOfCarries
    
if __name__ == '__main__':
    N = int(input('N: '))
    #M = int(input('M: '))
    numOfCarriesAdd = 0
    maxOfCarriesAdd = 0
    numOfCarriesMul = 0
    maxOfCarriesMul = 0
    for n in range(N+1):
        for m in range(N+1):
            numOfCarriesAdd = add(n, m)
            numOfCarriesMul = mul(n, m)
            if numOfCarriesAdd==1:# and numOfCarriesAdd > maxOfCarriesAdd:
                maxOfCarriesAdd += 1
    #for n in range(N+1):
        #for m in range(M+1):
                if numOfCarriesMul==2:# and numOfCarriesMul > maxOfCarriesMul:
                    maxOfCarriesMul += 1
                    #print('n:', n)
                    #print('m:', m)
    print(maxOfCarriesAdd)
    print(maxOfCarriesMul)