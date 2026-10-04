def print_pyramid(height: int) -> None:
    """
    
    >>> print_pyramid(1)
    #
    
    >>> print_pyramid(2)
      ##
     ###
    
    >>> print_pyramid(3)
      ##
     ###
    ####
    """
    print('#', end='')
    
if __name__ == '__main__':
    height = int(input("Hoe hoog moet de piramide zijn? "))
    while height <= 0 or height > 23:
        height = int(input("Hoe hoog moet de piramide zijn? "))
    print_pyramid(height)