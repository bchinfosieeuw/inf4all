def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.
    """
    jaren = 0
    while :
        increase = start_size // 3
        decrease = start_size // 4
        start_size += increase - decrease
        end_size = 
    return jaren

if __name__ == '__main__':
    start_size = int(input('Startgrootte: '))
    end_size = int(input('Eindgrootte: '))
    jaren = calculate_years(start_size, end_size)
    print("Jaren:", jaren)