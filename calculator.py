def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    """
    if y=="+":
        return float(x + z)
    elif y=="-":
        return x - z
    elif y=="*":
        return x * z
    elif y=="/":
        return x // z

if __name__ == '__main__':
    formula = input()
    x, y, z = formula.split(" ")
    resultaat = evaluate(int(x), y, int(z))
    print(resultaat)