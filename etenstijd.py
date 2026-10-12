def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    
    >>> meal(7:15)
    Het is tijd voor ontbijt
    
    >>> meal(08:00)
    Het is tijd voor ontbijt
    
    >>> meal(13:00)
    Het is tijd voor lunch
    
    >>> meal(18:53)
    Het is tijd voor avondeten
    
    >>> meal(22:12)
    """
    if time[0]=="0":
        if time[1]=="7" or (time[1]=="8" and time[-1]=="0" and time[-2]=="0"):
            return "ontbijt"
    else:
        if time[1]==":":
            if time[0]=="7" or (time[0]=="8" and time[-1]=="0" and 
            time[-2]=="0"):
                return "ontbijt"
        elif time[2]==":":
            if (time[0]=="1" and time[1]=="2") or (time[0]=="1" and time[1]=="3" and time[-1]=="0" and time[-2]=="0"):
                return "lunch"
            elif (time[0]=="1" and time[1]=="8") or (time[0]=="1" and time[1]=="9" and time[-1]=="0" and time[-2]=="0"):
                return "avondeten"

if __name__ == '__main__':
    time = input("Hoe laat is het? ")
    maaltijd = meal(time)
    if maaltijd!=None:
        print("Het is tijd voor", maaltijd)