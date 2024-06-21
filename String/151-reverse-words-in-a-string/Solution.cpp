
class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());

        int n = s.size();
        int start = 0;
        int end = 0;
        int i = 0;

        while (i < n && s[i] == ' ') i++;

        if (i == n) return ""; // If the string contains only spaces, return an empty string

        while (i < n) {
            // Skip leading spaces
            while (i < n && s[i] == ' ') i++;

            // If we reach the end of the string, break the loop
            if (i == n) break;

            // Update start to the beginning of the word
            start = end;

            // Copy the word to the current position
            while (i < n && s[i] != ' ') {
                s[end++] = s[i++];
            }

            // Reverse the word
            reverse(s.begin() + start, s.begin() + end);

            // Add a space after the reversed word
            s[end++] = ' ';
        }

        // Resize the string to remove any extra spaces at the end
        s.resize(end - 1);

        return s;
    }
};
