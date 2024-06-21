class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Create a temporary vector to store rotated elements
        vector<int> temp(nums.size());

        // Rotate each element of nums and store it in the temporary vector
        for (int i = 0; i < nums.size(); i++) {
            // Calculate the new index after rotation using modulo operation
            // (i + k) % nums.size() ensures that the index wraps around if it exceeds the size of nums
            temp[(i + k) % nums.size()] = nums[i];
        }

        // Copy elements from the temporary vector back to nums
        nums = temp;
    }
};
