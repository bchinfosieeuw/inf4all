def print_pyramid(height: int) -> None:
    """
    """
    print('#', end='')
    
if __name__ == '__main__':
    height = int(input("Hoe hoog moet de piramide zijn? "))
    while height <= 0 or height > 23:
        height = int(input("Hoe hoog moet de piramide zijn? "))
    print_pyramid(height)