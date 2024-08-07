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

def insertAtKthPosition(head, new_data, k):
    new_node = Node(new_data)

    if k == 0:
        new_node.next = head
        return new_node  # New node becomes the new head

    current = head
    position = 0

    # Traverse to the (k-1)-th node
    while current is not None and position < k - 1:
        current = current.next
        position += 1

    if current is None:
        raise IndexError("The position is greater than the length of the list")

    # Insert new node at the k-th position
    new_node.next = current.next
    current.next = new_node

    return head

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

# Insert 5 at the 2nd position (0-based index)
k = 2
linked_list = insertAtKthPosition(linked_list, 5, k)
print(f"Linked list after inserting 5 at the {k}-th position:")
printLL(linked_list)
