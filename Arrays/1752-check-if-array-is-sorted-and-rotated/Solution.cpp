class Solution {
public:
    bool check(vector<int>& nums) {
        // Initialize a variable to count the number of times the array is rotated
        int count = 0;

        // Get the size of the array
        int n = nums.size();

        // Iterate through the array from the second element to the last
        for(int i = 1; i < n; i++){
            // If the current element is less than the previous one,
            // it indicates a rotation point. Increment the count.
            if(nums[i - 1] > nums[i]){
                count++;
            }
        }

        // Check if the last element is greater than the first one.
        // If true, it indicates another rotation point. Increment the count.
        if(nums[n - 1] > nums[0]){
            count++;
        }

        // If the count is less than or equal to 1, the array can be sorted by at most one rotation.
        // Return true in this case, indicating that the array is in non-decreasing order.
        // Otherwise, return false.
        return count <= 1;
    }
};
