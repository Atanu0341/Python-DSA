class Solution {
public:
    int search(vector<int>& nums, int target) {
        return recursive(nums, target, 0, nums.size()-1);
    }

    int recursive(vector<int> nums, int target, int start, int end) {

        //base case
        if(start > end) return -1;

        int mid = start + (end - start)/2;

        if(target == nums[mid]) return mid;

        if(target < nums[mid]) end = mid - 1;

        else start = mid + 1;
        return recursive(nums, target, start, end);
    }
};