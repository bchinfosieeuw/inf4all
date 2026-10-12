def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    
    >>> evaluate(1 + 1)
    2.0
    
    >>> evaluate(100 - 9)
    2.0
    
    >>> evaluate(1 + 1)
    2.0
    
    >>> evaluate(1 + 1)
    2.0
    """
    if y=="+":
        return float(x + z)
    elif y=="-":
        return float(x - z)
    elif y=="*":
        return float(x * z)
    elif y=="/":
        return float(x) / float(z)

if __name__ == '__main__':
    formula = input()
    x, y, z = formula.split(" ")
    resultaat = evaluate(int(x), y, int(z))
    print(resultaat)