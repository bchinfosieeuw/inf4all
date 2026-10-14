def convert(s: str) -> str:
    """
    Returns string with double exclamation-signs and questionmarks.
    
    >>> convert("check")
    "check"
    
    >>> convert('convertInput')
    'convert_input'
    
    >>> convert('readFromFile')
    'read_from_file'
    """
    result = ""
    for teken in s:
        if teken.isupper():
            result += "_"
        result += teken.lower()
    return result
    
if __name__ == '__main__':
    s = input(camelCase)
    print(convert(s))