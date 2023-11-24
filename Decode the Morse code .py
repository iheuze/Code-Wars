from preloaded import MORSE_CODE

def decode_morse(morse_code):
    words = morse_code.split('   ')  # Split words
    decoded_message = ''

    for word in words:
        letters = word.split(' ')  # Split letters within a word
        decoded_word = ''

        for letter in letters:
            if letter in MORSE_CODE:
                decoded_word += MORSE_CODE[letter]

        decoded_message += decoded_word + ' '

    return decoded_message.strip()  # Remove trailing space
