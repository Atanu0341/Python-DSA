class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    # Write your code here
    
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    
    return head