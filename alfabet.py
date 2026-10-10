def compare(word1: str, word2: str) -> int:
    """
    Decide which word comes first alphabetically.
    
    >>> compare("Taylor", "Lana")
    1
    
    >>> compare("shark", "sWoRd")
    -1
    
    >>> compare("Daantje", "Daan")
    1
    
    >>> compare("amanda", "Amanda")
    0
    """
    signed1 = 1;
    if len(word1) > len(word2):
        dummy = word1
        word1 = word2
        word2 = dummy
        signed1 = -1
    mymin = len(word1)
    if len(word2) < len(word1):
        mymin = len(word2)
    for i in range(mymin):
        if (word1[i].lower() == word2[i].lower()) and len(word1)==len(word2):
            print("", end="")
        else:
            if word1[i].lower() <= word2[i].lower():
                return -1*signed1
            elif word1[i].lower() > word2[i].lower():
                return 1*signed1
    return 0

if __name__ == '__main__':
    word1 = input("Woord 1:")
    word2 = "Lana"
    if len(word1) > len(word2):
        dummy = word1
        word1 = word2
        word2 = dummy
    myindex = compare(word1, word2)
    print("Woord 1:", word1)
    print("Woord 2:", word2)
    if myindex==-1:
        print(word1, "first")
    elif myindex==1:
        print(word2, "first")
    else:
        print("No need to decide!")