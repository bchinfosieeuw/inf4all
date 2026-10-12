def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    """
    i = 0
    if time[0]=="0":
        i = 1
    if time[1]==":":
        if time[0]=="7" or ()
    elif time[2]==":":
        print()

if __name__ == '__main__':
    time = input("Hoe laat is het?")
    maaltijd = meal(time)
    print(maaltijd)