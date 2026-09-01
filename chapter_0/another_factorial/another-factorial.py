# Insert your another_factorial() function here.
def another_factorial(n: int) -> int:
    """
    Compute n! (factorial) using a for loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        # handle negative input with an error
        raise ValueError("Error: negative input given to factorial().")

    p = 1  # think of p as the container that will represent my growing product
 
    # for every integer i between 1 and n, p = p * i 
    for i in range(1, n + 1): # adds 1 to i automatically 
        p = p * i
    return p 
