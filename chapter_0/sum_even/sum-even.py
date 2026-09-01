# Insert your sum_even() function here.
def sum_even(k: int) -> int:
    """
    Return the sum of all positive even integers up to and including k.
    Args:
        k: Upper bound (integer). Only positive even numbers ≤ k are summed.
    Returns:
        The sum 2 + 4 + ... + (largest even ≤ k). Returns 0 if k < 2.
    """
    if k < 0: 
        raise ValueError("Error: Negative k given to function.")

    s = 0 

    # solution 1
    """
    for j in range(2, k + 1): 
        # is j even?
        if j % 2 == 0: 
            # yes, so add it to sum
            s += j 
    """

    # solution 2 
    for j in range(2, k + 1, 2): # note: step size of 2 means that we add 2 to j every time through
        s += j 

    # solution 3 
    # 2 + 4 + ... + k = 2 * (1 + 2 + ... + k / 2)
    """
    use gauss
    return 2 * gauss_sum(k // 2)
    """

    return s
