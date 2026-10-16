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

def count_carries_and_double_carries(a: int, b: int):
    """
    Counts:
    1. Total carry occurrences during manual multiplication.
    2. Occurrences where carry is used consecutively twice.
    Works for integers up to 100.
    """
    # Input validation
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers.")
    if abs(a) > 100 or abs(b) > 100:
        raise ValueError("Inputs must be <= 100 in absolute value.")

    # Ignore sign for carry counting
    a, b = abs(a), abs(b)

    total_carries = 0
    double_carries = 0

    a_digits = list(map(int, str(a)))[::-1]  # Least significant digit first
    b_digits = list(map(int, str(b)))[::-1]

    # Simulate manual multiplication
    for bd in b_digits:
        carry = 0
        prev_carry = False  # Tracks if previous step had a carry
        for ad in a_digits:
            product = ad * bd + carry
            if product >= 10:
                total_carries += 1
                if prev_carry:  # Carry occurred in previous step too
                    double_carries += 1
                carry = product // 10
                prev_carry = True
            else:
                carry = 0
                prev_carry = False
        # If carry remains after finishing this row
        if carry > 0:
            total_carries += 1
            if prev_carry:
                double_carries += 1

    return total_carries, double_carries
    
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
    N = 99
    numOfCarriesAdd = 0
    maxOfCarriesAdd = 0
    numOfCarriesMul = 0
    maxOfCarriesMul = 0
    for n in range(N+1):
        for m in range(n, N+1):
            n=3
            m=2
            #n=76
            #m=19
            #n=64
            #m=16
            numofdigits_n = len(str(n))
            try:
                numOfCarriesAdd = count_carries_in_addition(n, m)
                #print(f"Number of carry operations add: {numOfCarriesAdd}")
                if numOfCarriesAdd==1:
                    try:
                        maxOfCarriesAdd += 1
                        #total, numOfCarriesMul = count_carries_and_double_carries(n, m)
                        numOfCarriesMul = count_carries_in_multiplication(n, m)
                        extra = 0
                        #print('len:', len(str(int(str(n)[-1])*int(str(m)[-1]))))
                        if len(str(int(str(n)[-1])*int(str(m)[-1])))==1:
                            extra = 0
                            print('hetis1')
                        elif len(str(int(str(n)[-1])*int(str(m)[-1])))==2:
                            extra = 1
                            print('hetis2')
                        #print(f"Number of carry operations mul: {numOfCarriesMul}")
                        if numOfCarriesMul==2:#total==3 and #numofdigits_n-1:
                            maxOfCarriesMul += 1
                            #print('n:', n)
                            #print('m:', m)
                            #break
                    except ValueError as e:
                        print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")
    print(maxOfCarriesAdd)
    print(maxOfCarriesMul)