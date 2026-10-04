def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.
    
    >>> calculate_years(1200, 1300)
    1
    
    >>> calculate_years(9, 18)
    8
    
    >>> calculate_years(20, 100)
    20
    """
    jaren = 0
    while end_size > start_size:
        increase = start_size // 3
        decrease = start_size // 4
        start_size += increase - decrease
        jaren += 1
    return jaren

if __name__ == '__main__':
    start_size = int(input('Startgrootte: '))
    while start_size < 9:
        start_size = int(input('Startgrootte: '))
    end_size = int(input('Eindgrootte: '))
    while end_size <= start_size:
        end_size = int(input('Eindgrootte: '))
    jaren = calculate_years(start_size, end_size)
    print("Jaren:", jaren)