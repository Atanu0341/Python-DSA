class Node:
    def __init__(self, data1):
        self.data = data1
        self.next = None

def convertArrtoLL(arr):
    if not arr: # If the array is empty, it will return None
        return None
    
    head = Node(arr[0])

    return head

def print_head(head):
    if head:
        print(head.data)
    else:
        print("The linked list is empty.")


arr = [2, 5, 8, 9]


# Convert array to linked list
linked_list_head = convertArrtoLL(arr)

# print(linked_list_head)  it will print a default representation of the Node object, which includes the type of the object and its memory address.

# Print the head node
print_head(linked_list_head)