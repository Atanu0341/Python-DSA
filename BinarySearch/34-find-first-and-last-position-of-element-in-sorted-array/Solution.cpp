class Solution {
    int firstOccurrence(vector<int>& nums, int target){
        int start = 0;
        int end = nums.size() - 1;
        int ans = -1;

        int mid = start + (end - start)/2;

        while(start<=end){
            if(nums[mid]==target){
                ans=mid;
                end = mid - 1;
            }
            else if(nums[mid]<target){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }

            mid = start + (end - start)/2;
        }

        return ans;
    }

    int lastOccurrence(vector<int>& nums, int target){
        int start = 0;
        int end = nums.size() - 1;
        int ans = -1;

        int mid = start + (end - start)/2;

        while(start<=end){
            if(nums[mid]==target){
                ans=mid;
                start = mid + 1;
            }
            else if(nums[mid]<target){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }

            mid = start + (end - start)/2;
        }

        return ans;
    }



public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = firstOccurrence(nums, target);
        int last = lastOccurrence(nums, target);
        return {first, last};
    }
};