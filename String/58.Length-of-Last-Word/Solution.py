class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         # Split the string into words
        words = s.split()
    
    # If there are no words, return 0
        if not words:
            return 0
    
    # Return the length of the last word
        return len(words[-1])

        