from typing import *


def swapnigPositions(nums, start, end):

  # using two pointer
    # we need to swap the elements till n/2 indexes

    if start >= end:

        return

    else:

        nums[start], nums[end] = nums[end], nums[start]

        swapnigPositions(nums, start+1, end-1)

    return nums


def reverseArray(n: int, nums: List[int]) -> List[int]:

    return swapnigPositions(nums, 0, n - 1)
