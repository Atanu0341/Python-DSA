class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
# Creating a new Node with the value from the array
y = Node(2)
# Printing the data stored in the Node
print(y.data)