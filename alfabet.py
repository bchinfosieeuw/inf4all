def compare(word1: str, word2: str) -> int:
    """
    Decide which word is the first alphabetically.
    
    
    """
    for i in min(len(word1), len(word2)):
        if word1[i].lower() < word2[i].lower():
            return -1
        elif word1[i].lower() > word2[i].lower():
            return 1
        #elif word1[i].lower() == word2[i].lower():
    return 0

if __name__ == '__main__':
    myindex = compare("Taylor", "Lana")
    if index==-1:
        print("Woord 1:", word1)
    elif index==-1:
        print("Woord 2:")
    else:
        print("No need to decide!")