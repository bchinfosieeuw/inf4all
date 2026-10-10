def compare(word1: str, word2: str) -> int:
    """
    Decide which word is the first alphabetically.
    
    >>> compare("Taylor", "Lana")
    1
    
    >>> compare("shark", "sWoRd")
    -1
    
    >>> compare("Daantje", "Daan")
    1
    
    >>> compare("amanda", "Amanda")
    shark
    """
    for i in range(min(len(word1), len(word2))):
        if (word1[i].lower() == word2[i].lower()) and len(word1)==len(word2):
            print("", end="")
        else:
            if word1[i].lower() <= word2[i].lower():
                return -1
            elif word1[i].lower() > word2[i].lower():
                return 1
    return 0

if __name__ == '__main__':
    word1 = "amanda"
    word2 = "Amanda"
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