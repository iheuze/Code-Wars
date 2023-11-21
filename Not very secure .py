import re

def alphanumeric(password):
    # Use regular expression to check if the password is alphanumeric
    return bool(re.match("^[a-zA-Z0-9]+$", password))
