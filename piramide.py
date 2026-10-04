def print_pyramid(height: int) -> None:
    """
    """
    print('#', end='')
    
if __name__ == '__main__':
    height = int(input("Enter height of pyramid: "))
    while height <= 0 or height:
        height = int(input("Enter height of pyramid: "))
    print_pyramid(height)