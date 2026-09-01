# Insert your factorial() function here.
def factorial(n: int) -> int:
    """
    Compute n! (factorial) using a while loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    """
    if n < 0:
        # handle negative input with an error
        raise ValueError("Error: negative input given to factorial().")

    p = 1  # think of p as the container that will represent my growing product
    i = 1  # this is a counter variable to keep track of how many multiplications we've done

    while i <= n: 
        p = p * i  # left side: variable, right side: value
        i = i + 1  # update the counter

    # we are here in the function when i > n
    return p 
