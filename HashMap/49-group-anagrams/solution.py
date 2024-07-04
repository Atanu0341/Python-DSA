from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict with lists as default values to store grouped anagrams
        anagram_map = defaultdict(list)
        # Initialize an empty list to store the final grouped anagrams
        result = []

        # Iterate through each string in the input list
        for i in strs:
            # Sort the string and convert it to a tuple to use as a key in the dictionary
            sorted_s = tuple(sorted(i))
            # Append the original string to the list of anagrams corresponding to the sorted key
            anagram_map[sorted_s].append(i)

        # Iterate through the values in the anagram_map dictionary
        for value in anagram_map.values():
            # Append each list of grouped anagrams to the result list
            result.append(value)

        # Return the final list of grouped anagrams
        return result
