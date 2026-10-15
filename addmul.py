def add(n: int, m: int) -> int:
    numOfCarries = 0
    n1 = int(str(n)[-1])
    n10 = int(str(n)[-2])
    m1 = int(str(m)[-1])
    m10 = int(str(m)[-2])
    mybool1 = False
    for i in range (n):
        if mybool1==False:
            for j1 in range (m):
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