def comp(array1, array2):
    # Check if either array is None
    if array1 is None or array2 is None:
        return False

    # Square each element in array1 and sort the result
    squared_array1 = sorted(x**2 for x in array1)

    # Sort array2
    sorted_array2 = sorted(array2)

    # Check if the sorted squared array1 is equal to the sorted array2
    return squared_array1 == sorted_array2
