class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def convertArrToLL(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    return head

def insertAtHead(head, new_data):
    new_node = Node(new_data)  # Create a new node with the new_data
    new_node.next = head       # Point the new node to the current head
    return new_node            # New node becomes the new head

def printLL(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Initial array
arr = [2, 3, 1, 8]

# Convert array to linked list
linked_list = convertArrToLL(arr)
print("Original linked list:")
printLL(linked_list)

# Insert 5 at the head
linked_list = insertAtHead(linked_list, 5)
print("Linked list after inserting 5 at the head:")
printLL(linked_list)
