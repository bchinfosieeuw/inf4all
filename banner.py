def longest_word_from_list(lst: list[object]) -> str:
    """
    Determine the longest word from the list.
    
    >>> longest_word_from_list(['d', 'dd', 'ddd', 'dd'])
    'ddd'
    
    >>> longest_word_from_list(['Hallo', 'Zeker', 'Hoi'])
    'Hallo'
    
    >>> longest_word_from_list(['', '', 'ddd'])
    'ddd'
    """
    longest = ''
    prevlen = 0
    for i in range(len(lst)):
        if len(lst[i]) > prevlen:
            prevlen = len(lst[i])
            longest = lst[i]
    return longest
    
#print(longest_word_from_list(['d', 'dd', 'ddd', 'dd']))

def print_banner(lst: list[object]):
    """
    Print the items of the list, with recognition of the langest word.
    
    >>> print_banner(["Margherita", "Tutta", "la", "Vita"])
    ##########
    Margherita
    Tutta
    la
    Vita
    ##########
    
    >>> print_banner(["Hallo", "Hallo", "hallo", "Hallo", "Hallo"])
    #####
    Hallo
    Hallo
    hallo
    Hallo
    Hallo
    #####
    
    >>> print_banner(["Margherita"])
    ##########
    Margherita
    ##########
    """
    lengthlongest = len(longest_word_from_list(lst))
    for i in range(lengthlongest):
        print('#', end="")
    print()
    for i in range(len(lst)):
        print(lst[i])
    for i in range(lengthlongest):
        print('#', end="")
        
#print(print_banner(["Margherita", "Tutta", "la", "Vita"]))

def string_to_list(s: str) -> list[objects]:
    """
    >>> string_to_list(Dit is een stringetje.)
    ['Dit', 'is', 'een', 'stringetje.']
    """
    resultlist = []
    return resultlist
    
print(string_to_list('Dit is een stringetje.'))