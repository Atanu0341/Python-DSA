class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # Initialize an empty result string
        res = ""
        # Iterate through each string in the input list
        for s in strs:
            # For each string, append its length followed by '#' and the string itself to the result
            res += str(len(s)) + "#" + s
        # Return the encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # Initialize an empty list to store the decoded strings
        res = []
        # Initialize an index pointer for traversing the encoded string
        i = 0
        
        # Loop until the end of the encoded string is reached
        while i < len(s):
            # Set a pointer j to the current position of i
            j = i
            # Move j to find the position of the next '#'
            while s[j] != '#':
                j += 1
            # The length of the next string is between i and j
            length = int(s[i:j])
            # Move i to the character after '#'
            i = j + 1
            # Set j to the position after the end of the string
            j = i + length
            # Append the substring (the actual string) to the result list
            res.append(s[i:j])
            # Move i to the end of the current string
            i = j
            
        # Return the list of decoded strings
        return res