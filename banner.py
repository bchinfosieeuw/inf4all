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
    
    """
    lengthlongest
    print()
    
print(print_banner(["Margherita", "Tutta", "la", "Vita"]))