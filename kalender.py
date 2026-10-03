# 1 januari 1800 is een woensdag
START_DAY = 3
aantaldagenperjaarnietschrikkeljaar = 365
aantaldagenperjaarwelschrikkeljaar = 366

def is_leap_year(year: int) -> bool:
    """
    Return True als `year` een schrikkeljaar is.
    
    >>> is_leap_year(2024)
    True
    
    >>> is_leap_year(2023)
    False
    
    >>> is_leap_year(1900)
    False
    
    >>> is_leap_year(2000)
    True
    """
    if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
        return True
    else:
        return False

def days_from_1800(month: int, year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `month` of `year`.
    De eerste dag van `month` zit hier dus niet bij.
    Gebruikt `days_from_1800_until_year` en `days_until_month`.
    
    >>> days_from_1800(1, 1801)
    365
    
    >>> days_from_1800(1, 1804)
    1461
    
    >>> days_from_1800(month, year)
    
    """
    aantaldagen = days_from_1800_until_year(year)
    """print(aantaldagen)"""
    aantaldageninmaand = days_until_month(month, year)
    """print(aantaldageninmaand)"""
    return aantaldagen + aantaldageninmaand

def days_from_1800_until_year(year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `year`.
    1 januari van het nieuwe jaar is niet meegerekend.
    Gebruikt `is_leap_year`.
    
    >>> days_from_1800_until_year(year)
    
    
    >>> days_from_1800_until_year(year)
    
    
    >>> days_from_1800_until_year(year)
    
    """
    aantaldagen = 0
    for i in range(year-1800):
        if is_leap_year(i+1800+1):
            aantaldagen += aantaldagenperjaarwelschrikkeljaar
        else:
            aantaldagen += aantaldagenperjaarnietschrikkeljaar
    return aantaldagen

def days_until_month(month: int, year: int) -> int:
    """
    Telt het aantal dagen van 1 januari van `year` tot aan `month` van `year`.
    De dagen van `month` zitten hier dus niet bij.
    Gebruikt `days_in_month`.
    
    >>> days_until_month(month, year)
    
    
    >>> days_until_month(month, year)
    
    
    >>> days_until_month(month, year)
    
    """
    aantaldagentotmaand = 0
    for i in range(month-1):
        aantaldagentotmaand += days_in_month(i+1, year)
    return aantaldagentotmaand

def days_in_month(month: int, year: int) -> int:
    """
    Bepaalt het aantal dagen in `month` van `year`.
    Gebruikt `is_leap_year`.
    
    >>> days_in_month(month, year)
    
    
    >>> days_in_month(month, year)
    
    
    >>> days_in_month(month, year)
    
    """
    aantaldageninmaand = 0
    if month==1:
        aantaldageninmaand = 31
    elif month==2:
        if is_leap_year(year)==True:
            aantaldageninmaand = 29
        else:
            aantaldageninmaand = 28
    elif month==3:
        aantaldageninmaand = 31
    elif month==4:
        aantaldageninmaand = 30
    elif month==5:
        aantaldageninmaand = 31
    elif month==6:
        aantaldageninmaand = 30
    elif month==7:
        aantaldageninmaand = 31
    elif month==8:
        aantaldageninmaand = 31
    elif month==9:
        aantaldageninmaand = 30
    elif month==10:
        aantaldageninmaand = 31
    elif month==11:
        aantaldageninmaand = 30
    elif month==12:
        aantaldageninmaand = 31
    return aantaldageninmaand

def display_calendar(month: int, year: int) -> None:
    """
    Print de kalender.
    Gebruikt `display_header` en `display_grid`.
    
    >>> display_calendar(month, year)
    
    
    >>> display_calendar(month, year)
    
    
    >>> display_calendar(month, year)
    
    """
    display_header(month, year)
    display_grid(month, year)

def display_header(month: int, year: int) -> None:
    """
    Print de koptekst van de kalender.
    
    >>> display_header(month, year)
    
    
    >>> display_header(month, year)
    
    
    >>> display_header(month, year)
    
    """
    if month==1:
        monthtxt = 'Jan'
    elif month==2:
        monthtxt = 'Feb'
    elif month==3:
        monthtxt = 'Maa'
    elif month==4:
        monthtxt = 'Apr'
    elif month==5:
        monthtxt = 'Mei'
    elif month==6:
        monthtxt = 'Jun'
    elif month==7:
        monthtxt = 'Jul'
    elif month==8:
        monthtxt = 'Aug'
    elif month==9:
        monthtxt = 'Sep'
    elif month==10:
        monthtxt = 'Okt'
    elif month==11:
        monthtxt = 'Nov'
    elif month==12:
        monthtxt = 'Dec'
    print('Jaar: ', year)
    print('Maand: ', month)
    print('         ', monthtxt, year)
    print('---------------------------')
    print('Zon Maa Din Woe Don Vri Zat')

def display_grid(month: int, year: int) -> None:
    """
    Print het grid van de kalender.
    Gebruikt `first_weekday_month` en `days_in_month`.
    
    >>> display_grid(month, year)
    
    
    >>> display_grid(month, year)
    
    
    >>> display_grid(month, year)
    
    """
    index = first_weekday_month(month, year)
    """print(index)"""
    indexplus = 0
    minus1 = 0
    spaces = 4*index
    for i in range(spaces):
        print(" ", end="")
    print(1, end="")
    for j in range(3):
        print(" ", end="")
    if index==6:
        print("")
    for i in range(days_in_month(month, year)-1):
        print(i+2, end="")
        for j in range(3-minus1):
            print(" ", end="")
            if i==10-3:
                minus1 = 1
        if (index+i+1+7)%(7)==6:
            print("")

def first_weekday_month(month: int, year: int) -> int:
    """
    Bepaalt de eerste weekdag van de maand.
    Gebruikt `days_from_1800`.
    
    >>> first_weekday_month(1, 1800)
    3
    
    >>> first_weekday_month(2, 1800)
    6
    
    >>> first_weekday_month(3, 1800)
    1
    """
    aantaldagen = days_from_1800(month, year)
    index = (aantaldagen + START_DAY) % 7
    return index

if __name__ == '__main__':
    year = int(input("Jaar: "))
    month = int(input("Maand: "))
    display_calendar(month, year)
    print(days_from_1800(1, 1804))