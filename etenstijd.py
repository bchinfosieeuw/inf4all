def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    """
    if time[1]

if __name__ == '__main__':
    time = input("Hoe laat is het?")
    maaltijd = meal(time)
    print(maaltijd)