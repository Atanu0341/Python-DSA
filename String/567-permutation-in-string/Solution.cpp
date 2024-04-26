class Solution {
private:
    bool checkEqual(int a[26], int b[26]) {
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }
public:
    bool checkInclusion(string s1, string s2) {
        // Character count array
        int count1[26] = {0};

        for (char c : s1) {
            count1[c - 'a']++;
        }

        // Traverse s2 string in a window of size s1 length and compare
        int windowSize = s1.length();
        int count2[26] = {0};

        // Initialize variable i
        int i = 0;

        // Running for the first window
        while (i < windowSize && i < s2.length()) {
            count2[s2[i] - 'a']++;
            i++;
        }

        if (checkEqual(count1, count2)) {
            return true;
        }

        // Sliding window approach
        for (int i = windowSize; i < s2.length(); i++) {
            // Add new character to the window
            count2[s2[i] - 'a']++;

            // Remove old character from the window
            count2[s2[i - windowSize] - 'a']--;

            if (checkEqual(count1, count2)) {
                return true;
            }
        }

        return false; // Return false if no match found
    }
};
