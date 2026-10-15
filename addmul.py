def add(n: int, m: int) -> int:
    i = 0
    numOfCarries = 0
    while i < len(s):
        result += s[i]
        if s[i] in "!?":
            result += s[i]
        i += 1
    return numOfCarries
    
if __name__ == '__main__':
    s = input()
    print(yell(s))