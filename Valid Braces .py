def valid_braces(string):
    stack = []
    opening_braces = {'(', '[', '{'}
    closing_braces = {')', ']', '}'}
    brace_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in opening_braces:
            stack.append(char)
        elif char in closing_braces:
            if not stack or brace_pairs[stack.pop()] != char:
                return False

    return not stack
