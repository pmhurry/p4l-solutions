def min_integer_array(lst: list[int]) -> int:
    """
    Return the minimum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The smallest integer in lst.
    Raises:
        ValueError: If lst is empty.
    """
    if len(lst) == 0: 
        raise ValueError("Error: empty list given to function.")

    m = lst[0] # stores our minimum

    for val in lst: 
        # is current value better than what I currently have?
        if val < m: 
            # update m appropriately
            m = val

    return m
