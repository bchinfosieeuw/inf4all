def longest_word_from_list(lst: list[object]) -> str:
    """
    Determine the longest word from the list.
    
    >>> longest_word_from_list(['d', 'dd', 'ddd', 'dd'])
    ddd
    """
    longest = ''
    prevlen = 0
    for i in range(len(lst)):
        if len(lst[i]) > prevlen:
            prevlen = 
            longest = lst[i]
    return longest
    
longest_word_from_list(['d', 'dd', 'ddd', 'dd'])