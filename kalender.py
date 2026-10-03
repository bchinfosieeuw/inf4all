# 1 januari 1800 is een woensdag
START_DAY = 3
aantaldagenperjaarnietschrikkeljaar = 365
aantaldagenperjaarwelschrikkeljaar = 364

def is_leap_year(year: int) -> bool:
    """
    Return True als `year` een schrikkeljaar is.
    """

def days_from_1800(month: int, year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `month` of `year`.
    De eerste dag van `month` zit hier dus niet bij.
    Gebruikt `days_from_1800_until_year` en `days_until_month`.
    """

def days_from_1800_until_year(year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `year`.
    1 januari van het nieuwe jaar is niet meegerekend.
    Gebruikt `is_leap_year`.
    """

def days_until_month(month: int, year: int) -> int:
    """
    Telt het aantal dagen van 1 januari van `year` tot aan `month` van `year`.
    De dagen van `month` zitten hier dus niet bij.
    Gebruikt `days_in_month`.
    """

def days_in_month(month: int, year: int) -> int:
    """
    Bepaalt het aantal dagen in `month` van `year`.
    Gebruikt `is_leap_year`.
    """

def display_calendar(month: int, year: int) -> None:
    """
    Print de kalender.
    Gebruikt `display_header` en `display_grid`.
    """
    display_header(month, year)

def display_header(month: int, year: int) -> None:
    """
    Print de koptekst van de kalender.
    """
    print('Jaar: ', year)
    print('Maand: ', month)
    print('          ', yeartxt, ' ', )
    print('Maand jaar')
    print('---------------------------')
    print('Zon Maa Din Woe Don Vri Zat')

def display_grid(month: int, year: int) -> None:
    """
    Print het grid van de kalender.
    Gebruikt `first_weekday_month` en `days_in_month`.
    """

def first_weekday_month(month: int, year: int) -> int:
    """
    Bepaalt de eerste weekdag van de maand.
    Gebruikt `days_from_1800`.
    """

if __name__ == '__main__':
    year = int(input("Jaar: "))
    month = int(input("Maand: "))
    display_calendar(month, year)