def trivial_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using the "trivial" (brute-force) algorithm.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The non-negative GCD of a and b. 
    """
    d = 1
    m = min_2(a, b)
    for p in range(1, m + 1):
        # how do I check that p is a divisor of both a and b?
        if (a % p == 0) and (b % p == 0):
            # I can only be here if p is a divisor of both  
            d = p  

    return d

# Place your min_2() subroutine here.
def min_2(a: int, b: int) -> int: 
    """
    Takes two integers and returns their minimum.

    Parameters:
    - a (int)
    - b (int)

    Returns:
    int: minimum of a and b
    """
    if a < b: 
        return a  # a is smaller
    else:  # b is greater than or equal to a 
        return b  
