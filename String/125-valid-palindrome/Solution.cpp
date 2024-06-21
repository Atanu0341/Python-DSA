class Solution {
private:
    bool valid(char ch) {
        // Check if the character is alphanumeric
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9')) {
            return true;
        }
        return false;
    }

    char toLowerCase(char ch) {
        // Convert the character to lowercase
        if (ch >= 'A' && ch <= 'Z') {
            return ch - 'A' + 'a';
        }
        return ch;
    }

    bool checkPalindrome(string a) {
        int start = 0;
        int end = a.size() - 1;

        while (start < end) {
            // Move the start pointer until it points to an alphanumeric character
            while (start < end && !valid(a[start])) {
                start++;
            }
            // Move the end pointer until it points to an alphanumeric character
            while (start < end && !valid(a[end])) {
                end--;
            }
            // If the characters are not equal (ignoring case), return false
            if (toLowerCase(a[start]) != toLowerCase(a[end])) {
                return false;
            }
            // Move the pointers
            start++;
            end--;
        }
        // If the loop completes without finding any mismatch, the string is a palindrome
        return true;
    }

public:
    bool isPalindrome(string s) {
        string temp = "";

        // Remove non-alphanumeric characters and convert to lowercase
        for (int j = 0; j < s.length(); j++) {
            if (valid(s[j])) {
                temp.push_back(s[j]);
            }
        }

        // Check if the modified string is a palindrome
        return checkPalindrome(temp);
    }
};
