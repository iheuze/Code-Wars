def next_smaller(n):
    digits = list(str(n))
    i = len(digits) - 2

    # Find the first pair of digits where digits[i] > digits[i + 1]
    while i >= 0 and digits[i] <= digits[i + 1]:
        i -= 1

    # If no such pair is found, it means the number is already the smallest
    if i == -1:
        return -1

    # Find the rightmost digit smaller than digits[i] in the suffix
    j = len(digits) - 1
    while digits[j] >= digits[i]:
        j -= 1

    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the suffix to get the smallest number
    digits[i + 1:] = reversed(digits[i + 1:])

    result = int(''.join(digits))

    # Check if the result has the same number of digits and does not have a leading zero
    return result if len(str(result)) == len(digits) and str(result)[0] != '0' else -1
