class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Initialize an empty dictionary to store frequencies of each element
        frequencies = {}

        # Calculate frequencies of each element in nums
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        # Find the maximum frequency among all elements
        max_frequency = 0
        for frequency in frequencies.values():
            max_frequency = max(max_frequency, frequency)

        # Count how many elements have the maximum frequency
        count_frequency = 0
        for frequency in frequencies.values():
            if frequency == max_frequency:
                count_frequency += 1

        # Return the product of count_frequency and max_frequency
        return count_frequency * max_frequency
