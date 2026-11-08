def split_capitalized(strs: list[str]) -> list[list[str]]:
    """
    >>> split_capitalized['Adam', 'fiets', 'Utr', '']
    [['Adam', 'Utr'], ['fiets', '']]
    
    >>> split_capitalized['Hallo', 'Hallo', 'hallo', 'hoi']
    [['Hallo', 'Hallo'], ['hallo', 'hoi']]
    
    >>> split_capitalized['Doei', 'Doei', 'Doei', 'Doei']
    [['Doei', 'Doei', 'Doei', 'Doei'], []]
    
    >>> split_capitalized['ja', 'ja', 'nee', 'nee']
    [[], ['ja', 'ja', 'nee', 'nee']]
    """
    hoofdletter = []
    rest = []
    for i in range(len(strs)):
        if strs[i]!='' and strs[i][0].isupper()==True:
            hoofdletter.append(strs[i])
        else:
            rest.append(strs[i])
    return [hoofdletter, rest]
    
#print(split_capitalized(['Adam', 'fiets', 'Utr', '']))
#print(split_capitalized(['Doei', 'Doei', 'Doei', 'Doei']))

def repeat_chars(s: str, counts: list[int]) -> str:
    """
    >>> repeat_chars('abcd', [2, 0, 3])
    'aacccd'
    
    >>> repeat_chars('aba', [2, 1, 3])
    'aabaaa'
    
    >>> repeat_chars('abc', [2, 0, 3])
    'aaccc'
    
    >>> repeat_chars('abcd', [2, 0, 3, 4, 5])
    'aacccdddd'
    """
    result = ''
    diff = len(s) - len(counts)
    mycounts = []
    if diff < 0:
        for i in range(len(s)):
            mycounts.append(counts[i])
        counts = mycounts
    for i in range(len(counts)):
        if counts[i].is_integer():
            for j in range(counts[i]):
                result += s[i]
        else:
            result += s[i]
    if diff > 0:
        for i in range(len(s)-diff, len(s)):
            result += s[i]
    return result

#print(repeat_chars('abcd', [2, 0, 3]))
#print(repeat_chars('abcd', [2, 0, 3, 4, 5]))

def reverse_long_words(sentence: str, n: int) -> str:
    """
    >>> reverse_long_words('dit is een lange zin.', 3)
    'dit is een egnal zin.'
    
    >>> reverse_long_words('dit is een lange zin.', 4)
    'dit is een egnal zin.'
    
    >>> reverse_long_words('dit is een lange lange zin.', 3)
    'dit is een egnal zin.'
    
    >>> reverse_long_words('dit is een lange zin.', 3)
    'dit is een egnal zin.'
    """
    result = ''
    woord = ''
    dwoor = ''
    length = 0
    extra = 0
    myresult = ''
    for i in range(len(sentence)):
        woord += sentence[i]
        dwoor = sentence[i] + dwoor
        if sentence[i] in ". ":
            extra += 1
            i+=1
        if sentence[i-extra+1] in ". ":
            if length <= n+1:
                result += woord
            else:
                if length > 0:
                    mywoord = woord[length]
                woord = mywoord
                result += dwoor + " "
            woord = ''
            dwoor = ''
            length = 0
            extra = 0
        else :
            length += 1
    return result
    
print(reverse_long_words('dit is een lange lange zin.', 3))
    