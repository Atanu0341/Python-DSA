class Node:
    def __init__(self, data1):
        self.data = data1
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

def deleteTail(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one element, return None

    current = head
    while current.next.next is not None:  # Traverse to the second-to-last node
        current = current.next

    current.next = None  # Remove the last node
    return head

def printLL(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

arr = [1, 8, 1, 3]

# Convert array to linked list and print it
linked_list = convertArrToLL(arr)
print("Original linked list:")
printLL(linked_list)

# Delete the tail of the linked list and print the updated list
deleted_tail = deleteTail(linked_list)
print("Linked list after deleting the tail:")
printLL(deleted_tail)
