class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty dictionary to store frequency of each number
        frequency = {}
        
        # Iterate through each number in the list
        for i in nums:
            # Check if the number is already in the dictionary
            if i in frequency:
                # If the number is already in the dictionary, it means we have found a duplicate
                return True
            # If the number is not in the dictionary, add it with a frequency of 1
            frequency[i] = 1
        
        # If we finish iterating through the list without finding any duplicates, return False
        return False
