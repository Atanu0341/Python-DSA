class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # Step 1: Store the reference to the next node in a temporary variable.
        temp = node.next
        
        # Step 2: Copy the value from the next node into the current node.
        # This effectively replaces the value of the current node with the value of the next node.
        node.val = temp.val
        
        # Step 3: Adjust the next pointer of the current node to skip the next node.
        # This connects the current node directly to the node after the next node.
        node.next = temp.next
        
        # Step 4: Optional clean-up for the node that has been effectively removed.
        # Setting temp.next to None helps in garbage collection.
        temp.next = None
