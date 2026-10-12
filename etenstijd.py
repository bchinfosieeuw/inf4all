def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    """
    i = 0
    if time[0]=="0":
        
    else:
        if time[1]==":":
            if time[0]=="7" or (time[0]=="8" and time[-1]=="0" and time[-2]=="0"):
                return "ontbijt"
        elif time[2]==":":
            if (time[0]=="1" and time[1]=="2") or (time[0]=="1" and time[1]=="3" and time[-1]=="0" and time[-2]=="0"):
                return "lunch"
            elif (time[0]=="1" and time[1]=="8") or (time[0]=="1" and time[1]=="9" and time[-1]=="0" and time[-2]=="0"):
                return "avondeten"

if __name__ == '__main__':
    time = input("Hoe laat is het? ")
    maaltijd = meal(time)
    print(maaltijd)