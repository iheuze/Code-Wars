def sum_two_smallest_numbers(numbers):
    # Sort the array in ascending order
    sorted_numbers = sorted(numbers)
    
    # Take the sum of the first two elements (the two smallest numbers)
    result = sorted_numbers[0] + sorted_numbers[1]
    
    return result
