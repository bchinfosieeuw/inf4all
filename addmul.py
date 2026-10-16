def count_carries_in_addition(a: int, b: int) -> int:
    """
    Count the number of carry operations when adding two integers.
    Works for integers up to 100 (and beyond).
    """
    # Input validation
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")
    if a > 100 or b > 100:
        raise ValueError("Inputs must be <= 100.")

    carry_count = 0
    carry = 0

    # Simulate manual addition
    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        if digit_a + digit_b + carry >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10

    return carry_count
    
def count_carries_in_multiplication(a: int, b: int) -> int:
    """
    Counts the number of carry operations during manual multiplication of two integers.
    Works for integers up to 100 (but can handle larger too).
    """
    # Input validation
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers.")
    if abs(a) > 100 or abs(b) > 100:
        raise ValueError("Inputs must be <= 100 in absolute value.")

    # Handle negatives by ignoring sign for carry counting
    a, b = abs(a), abs(b)

    carries = 0
    a_digits = list(map(int, str(a)))[::-1]  # Reverse for least significant digit first
    b_digits = list(map(int, str(b)))[::-1]

    # Simulate manual multiplication
    for i, bd in enumerate(b_digits):
        carry = 0
        for ad in a_digits:
            product = ad * bd + carry
            if product >= 10:
                carries += 1
                carry = product // 10
            else:
                carry = 0
        # If carry remains after finishing this row, count it
        if carry > 0:
            carries += 1

    return carries
    
if __name__ == '__main__':
    N = int(input('Enter a maximum number: '))
    numOfCarriesAdd = 0
    maxOfCarriesAdd = 0
    numOfCarriesMul = 0
    maxOfCarriesMul = 0
    for n in range(N+1):
        for m in range(N+1):
            try:
                numOfCarriesAdd = count_carries_in_addition(n, m)
                extra = 0
                if len(str(int(str(n)[-1])*int(str(m)[-1])))==1:
                    extra = 0
                elif len(str(int(str(n)[-1])*int(str(m)[-1])))==2:
                    extra = 1
                if numOfCarriesAdd==1:
                    try:
                        maxOfCarriesAdd += 1
                        numOfCarriesMul = count_carries_in_multiplication(n, m)
                        if numOfCarriesMul==2+extra:#and n != m #and n
                            maxOfCarriesMul += 1
                            print('n:', n)
                            print('m:', m)
                    except ValueError as e:
                        print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")
    print(maxOfCarriesAdd)
    print(maxOfCarriesMul)