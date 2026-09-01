# Insert your sum_first_n_integers() function here.
def sum_first_n_integers(n: int) -> int:
    """
    Return the sum of the first n positive integers using a while loop.
    Args:
        n: The number of initial positive integers to sum (must be non-negative).
    Returns:
        The sum 1 + 2 + ... + n. Returns 0 if n == 0.
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        # handle negative input with an error
        raise ValueError("Error: negative input given to sum_first_n_integers().")

    s = 0
    i = 1  # counter variable 
    while i <= n: 
        s += i  # this is shorthand for s = s + i
        i += 1  # shorthand for i = i + 1 (Python doesn't have i++)

    # also: s *= i, s /= i, s -= i

    # at this point, we know that i > n

    return s
