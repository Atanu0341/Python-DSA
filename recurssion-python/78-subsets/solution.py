class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate_subsets(index):
            if index >= len(nums):
               ans.append(current[:])
               return

            current.append(nums[index]) 
            generate_subsets(index+1)
            current.pop()
            generate_subsets(index+1)
        
        ans = []
        current = []
        generate_subsets(0)
        return ans
        