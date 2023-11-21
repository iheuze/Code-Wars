def get_sum(a, b):
    # Ensure a is the smaller of the two numbers
    if a > b:
        a, b = b, a
    
    # Use the sum formula for an arithmetic series
    return sum(range(a, b + 1))
