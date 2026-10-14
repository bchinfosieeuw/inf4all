def convert(s: str) -> str:
    """
    Converts string format from camelCase to .
    
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
    s = input('camelCase: ')
    print('snake_case:', convert(s))