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
        result += teken
        if teken not in "_":
            result += "_"
    return result
    
if __name__ == '__main__':
    s = input()
    print(convert(s))