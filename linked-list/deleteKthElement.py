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

def deleteKthElement(head, k):
    if head is None:
        return None  # Empty list, nothing to delete
    
    if k == 0:
        return head.next  # If k is 0, delete the head
    
    current = head
    count = 0
    
    # Traverse to the (k-1)th node
    while current is not None and count < k - 1:
        current = current.next
        count += 1
    
    # If k is out of bounds
    if current is None or current.next is None:
        return head
    
    # Delete the kth node
    current.next = current.next.next
    
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

# Delete the k-th element of the linked list and print the updated list
k = 2
deleted_kth = deleteKthElement(linked_list, k)
print(f"Linked list after deleting the {k}-th element:")
printLL(deleted_kth)
