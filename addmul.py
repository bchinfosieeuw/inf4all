def yell(s: str) -> str:
    i = 0
    result = ""
    while i < len(s):
        result += s[i]
        if s[i] in "!?":
            result += s[i]
        i += 1
    return result
    
if __name__ == '__main__':
    s = input()
    print(yell(s))