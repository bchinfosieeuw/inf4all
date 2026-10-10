def compare(word1: str, word2: str) -> int:
    """
    Decide which word is the first alphabetically.
    
    
    """
    for i in min(len(word1), len(word2)):
        if word1[i].lower() < word2[i].lower():
            return -1
        elif word1[i].lower() > word2[i].lower():
            return -1
        elif word1[i].lower() == word2[i].lower():
            return -1

if __name__ == '__main__':
    compare("Taylor", "Lana")