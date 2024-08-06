class Node:
    def __init__(self, data1):
        self.data = data1
        self.next = None

def convertArrtoLL(arr):
    if not arr:  # If the array is empty, return None
        return None
    
    head = Node(arr[0])  # Create the head node with the first element of the array
    current = head       # Initialize the current node to the head

    for value in arr[1:]:  # Iterate through the rest of the array
        current.next = Node(value)  # Create a new node and link it to the current node
        current = current.next      # Move to the newly created node

    return head  # Return the head of the linked list

def print_linked_list(head):
    # Initialize the current node to the head of the linked list
    current = head
    
    # Traverse the linked list
    while current:
        # Print the data of the current node
        # Use " -> " if there is a next node, otherwise use a newline
        print(current.data, end=" -> " if current.next else "\n")
        
        # Move to the next node in the linked list
        current = current.next


arr = [2, 5, 8, 9]

# Convert array to linked list
linked_list_head = convertArrtoLL(arr)

# Print the linked list
print_linked_list(linked_list_head)