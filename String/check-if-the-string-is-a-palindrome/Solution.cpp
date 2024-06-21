#include <bits/stdc++.h> 
char toLowerCase(char ch) {
    return tolower(ch); // Use the standard library function tolower
}

// Function to check if a character is alphanumeric
bool isAlphanumeric(char ch) {
    return isalnum(ch); // Use the standard library function isalnum
}

// Function to check if a string is a palindrome
bool checkPalindrome(string s) {
    int start = 0;
    int end = s.size() - 1;

    while (start < end) {
        // Move the start pointer until it points to an alphanumeric character
        while (start < end && !isAlphanumeric(s[start])) {
            start++;
        }
        // Move the end pointer until it points to an alphanumeric character
        while (start < end && !isAlphanumeric(s[end])) {
            end--;
        }
        // If the characters are not equal (ignoring case), return false
        if (toLowerCase(s[start]) != toLowerCase(s[end])) {
            return false;
        }
        // Move the pointers
        start++;
        end--;
    }
    // If the loop completes without finding any mismatch, the string is a palindrome
    return true;
}