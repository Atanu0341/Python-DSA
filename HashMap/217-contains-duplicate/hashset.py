class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to keep track of seen numbers
        hashset = set()
        
        # Iterate through each number in the list
        for i in nums:
            # Check if the number is already in the set
            if i in hashset:
                # If it is, we found a duplicate, so return True
                return True
            # If it's not, add the number to the set
            hashset.add(i)
        
        # If we complete the loop without finding duplicates, return False
        return False
