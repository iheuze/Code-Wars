def first_non_repeating_letter(s):
    # Convert the string to lowercase for case-insensitive comparison
    lower_s = s.lower()

    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the lowercase version of the character is unique in the string
        if lower_s.count(char.lower()) == 1:
            return char

    # If no non-repeating character is found, return an empty string
    return ''

