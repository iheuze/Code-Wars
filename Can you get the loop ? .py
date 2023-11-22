class Node:
    def __init__(self):
        self.next = None

def loop_size(node):
    # Function to find the meeting point of two pointers
    def find_meeting_point(start):
        tortoise = hare = start
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise  # Meeting point found
        return None

    # Find the meeting point using Floyd's Tortoise and Hare algorithm
    meeting_point = find_meeting_point(node)
    if not meeting_point:
        return 0  # No loop

    # Find the length of the loop
    count = 1
    current = meeting_point.next
    while current != meeting_point:
        count += 1
        current = current.next

    return count

# Example usage
if __name__ == "__main__":
    # Create nodes and set up a linked list with a loop
    nodes = [Node() for _ in range(15)]
    for i in range(14):
        nodes[i].next = nodes[i + 1]
    nodes[14].next = nodes[6]

    # Find and print the loop size
    print(loop_size(nodes[0]))  # Output: 9
