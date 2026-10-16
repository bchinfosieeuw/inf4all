def add22(n: int, m: int) -> int:
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
    
def add23(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = 0
    if len(str(n))==2:
        n10 = int(str(n)[-2])
    m1 = 0
    m10 = 0
    if len(str(m))==3:
        m1 = int(str(m)[-2])
        m10 = int(str(m)[-3])
    
    if n10 + m1 >= 10:
        numOfCarries += 1
        if m10 + 1 >= 10:
            numOfCarries += 1
    elif m10 >= 10:
        numOfCarries += 1
    return numOfCarries
    
def add33(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = int(str(n)[-2])
    n100 = int(str(n)[-3])
    m1 = int(str(m)[-1])
    m10 = int(str(m)[-2])
    m100 = int(str(m)[-3])
    
    if n1 + m1 >= 10:
        numOfCarries += 1
        if m10 + 1 >= 10:
            numOfCarries += 1
    elif m10 >= 10:
        numOfCarries += 1
    return numOfCarries
    
def add24(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = 0
    if len(str(n))==2:
        n10 = int(str(n)[-2])
    m1 = 0
    m10 = 0
    if len(str(m))==4:
        m1 = int(str(m)[-3])
        m10 = int(str(m)[-4])
    
    if n10 + m1 >= 10:
        numOfCarries += 1
        if m10 + 1 >= 10:
            numOfCarries += 1
    elif m10 >= 10:
        numOfCarries += 1
    return numOfCarries
    
def add34(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = int(str(n)[-2])
    n100 = int(str(n)[-3])
    if len(str(n))==2:
        n10 = int(str(n)[-2])
    m1 = 0
    m10 = 0
    if len(str(m))==4:
        m1 = int(str(m)[-3])
        m10 = int(str(m)[-4])
    
    if n10 + m1 >= 10:
        numOfCarries += 1
        if m10 + 1 >= 10:
            numOfCarries += 1
    elif m10 >= 10:
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
    k2 = n1 * m10 * 10
    k3plus = k1 + k2
    k3 = n10 * m1 * 10
    k4plus = k3plus + k3
    k4 = n10 * m10 * 100
    
    if len(str(k1))<=2 and len(str(k2))<=2:
        numOfCarries += add22(k1, k2)
    elif len(str(k1))<=2 and len(str(k2))==3:
        numOfCarries += add23(k1, k2)
    else:
        print("halloA")
    if len(str(k3))<=2 and len(str(k3plus))<=2:
        numOfCarries += add22(k3, k3plus)
    elif len(str(k3))<=2 and len(str(k3plus))==3:
        numOfCarries += add23(k3, k3plus)
    elif len(str(k3))==3 and len(str(k3plus))==3:
        numOfCarries += add33(k3, k3plus)
    else:
        print("halloB")
    if len(str(k4plus))<=2 and len(str(k4))==3:
        numOfCarries += add23(k4plus, k4)
    elif len(str(k4plus))==3 and len(str(k4))==3:
        numOfCarries += add33(k4plus, k4)
    elif len(str(k4plus))<=2 and len(str(k4))==4:
        numOfCarries += add24(k4plus, k4)
    elif len(str(k4plus))==3 and len(str(k4))==4:
        numOfCarries += add34(k4plus, k4)
    else:
        print("halloC")
        
        
        
    #print("hallo:", numOfCarries)
    

    

            
    
    return numOfCarries
    
if __name__ == '__main__':
    N = 99
    numOfCarriesAdd = 0
    maxOfCarriesAdd = 0
    numOfCarriesMul = 0
    maxOfCarriesMul = 0
    for n in range(N+1):
        for m in range(N+1):
            #n=76
            #m=19
            numOfCarriesAdd = add22(n, m)
            numOfCarriesMul = mul(n, m)
            if numOfCarriesAdd==1:
                maxOfCarriesAdd += 1
                if numOfCarriesMul==2:
                    maxOfCarriesMul += 1
                    print('n:', n)
                    print('m:', m)
    #print(maxOfCarriesAdd)
    print(maxOfCarriesMul)