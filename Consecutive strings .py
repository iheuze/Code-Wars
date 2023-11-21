def longest_consec(strarr, k):
    n = len(strarr)

    # Check for invalid cases
    if n == 0 or k > n or k <= 0:
        return ""

    # Calculate the lengths of consecutive concatenations and find the index of the maximum length
    max_length_index = max(range(n - k + 1), key=lambda i: sum(len(strarr[j]) for j in range(i, i + k)))

    # Concatenate the strings starting from the calculated index
    result = ''.join(strarr[max_length_index:max_length_index + k])

    return result
