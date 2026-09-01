# Insert your min_2() function here.
def min_2(a: int, b: int) -> int:
    """
    Return the smaller of two integers.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The minimum of a and b.
    """
    if a < b: 
        return a  # a is smaller
    else:  # b is greater than or equal to a 
        return b 
