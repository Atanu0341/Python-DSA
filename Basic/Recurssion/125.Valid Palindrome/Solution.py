class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Helper function to check if a character is alphanumeric
        def is_alphanumeric(char):
            return char.isalnum()

        # Helper function to convert character to lowercase
        def to_lowercase(char):
            return char.lower()

        # Recursive function to check if string is palindrome
        def check_palindrome(i, j):
            # Base case: if left pointer surpasses or equals right pointer, return True
            if i >= j:
                return True
            
            # Move left pointer to the next alphanumeric character
            while i < j and not is_alphanumeric(s[i]):
                i += 1
            
            # Move right pointer to the next alphanumeric character
            while i < j and not is_alphanumeric(s[j]):
                j -= 1
            
            # If characters at both pointers are not equal (after converting to lowercase),
            # return False
            if to_lowercase(s[i]) != to_lowercase(s[j]):
                return False
            
            # Continue checking with updated pointers
            return check_palindrome(i + 1, j - 1)

        # Start checking palindrome from the beginning and end of the string
        return check_palindrome(0, len(s) - 1)