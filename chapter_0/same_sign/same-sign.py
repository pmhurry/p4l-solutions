# Insert your same_sign() function here.
def same_sign(x: int, y: int) -> bool:
    """
    Determine whether two integers have the same sign.
    Args:
        x: First integer.
        y: Second integer.
    Returns:
        True if x and y share the same sign (including both zero), False otherwise.
    """
    # three cases: 
    # 1. both positive (x * y >= 0, True)
    # 2. both negative (x * y >= 0, True)
    # 3. opposite signs (x * y < 0, False)

    return (x * y >= 0)
