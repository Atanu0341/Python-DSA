from typing import *

#  using single pointer

def swapping(i,n,nums):

    if i >= n // 2:

        return []

    nums[i] , nums[n-i-1] = nums[n-i-1],nums[i]

    swapping(i+1,n,nums)

    

    return nums

def reverseArray(n: int, nums: List[int]) -> List[int]:

     return swapping(0,n,nums)