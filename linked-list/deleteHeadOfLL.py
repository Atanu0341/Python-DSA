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

def deleteHead(head):
    if head is None:
        return None
    head = head.next
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

# Delete the head of the linked list and print the updated list
deleted_head = deleteHead(linked_list)
print("Linked list after deleting the head:")
printLL(deleted_head)
