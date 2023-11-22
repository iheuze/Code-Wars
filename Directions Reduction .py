def dir_reduc(arr):
    # Define opposite direction pairs
    opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}

    # Initialize a stack to keep track of the current path
    stack = []

    # Iterate through the directions
    for direction in arr:
        # Check if the current direction cancels the last direction in the stack
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            # If not, add the current direction to the stack
            stack.append(direction)

    return stack
