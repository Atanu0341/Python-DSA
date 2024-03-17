class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x) # Convert integer to string for easy comparison

        return x_str == x_str[::-1]

        