class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store numbers and their indices
        prevMap = {}  # values:index will store here

        # Iterate through the list 'nums' along with their indices
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target from the current number
            diff = target - n

            # Check if the required difference exists in the dictionary
            if diff in prevMap:
                # If found, return the indices of the two numbers that add up to the target
                return [prevMap[diff], i]

            # If the difference is not found in the dictionary, store the current number    and its index
            prevMap[n] = i

        # If no such pair is found after iterating through the entire list, return None
        return None