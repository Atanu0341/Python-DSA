'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    current = head
    length = 0

    # travese the linked list
    while current:
        # Move to the next node
        current = current.next

        # Increment the length counter
        length += 1

    return length


